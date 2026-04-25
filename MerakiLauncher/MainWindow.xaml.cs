using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Security.Cryptography;
using System.Threading.Tasks;
using System.Windows;
using System.Diagnostics;
using Newtonsoft.Json;

namespace MerakiLauncher
{
    public partial class MainWindow : Window
    {
        // DEFAULT CONFIGURATION (Overridden by config.json if exists)
        private string GITHUB_USER = "IamGustav-Student"; 
        private string GITHUB_REPO = "L2Meraki-Interlude";
        private string GITHUB_FOLDER = "client_updates";
        private string BASE_URL => $"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main/{(string.IsNullOrEmpty(GITHUB_FOLDER) ? "" : GITHUB_FOLDER + "/")}";
        
        private List<PatchFile> _filesToUpdate = new List<PatchFile>();

        public MainWindow()
        {
            InitializeComponent();
            LoadConfig();
            CheckUpdates();
        }

        private void LoadConfig()
        {
            if (File.Exists("config.json"))
            {
                try {
                    var cfg = JsonConvert.DeserializeObject<Dictionary<string, string>>(File.ReadAllText("config.json"));
                    if (cfg != null) {
                        if (cfg.ContainsKey("user")) GITHUB_USER = cfg["user"];
                        if (cfg.ContainsKey("repo")) GITHUB_REPO = cfg["repo"];
                        if (cfg.ContainsKey("folder")) GITHUB_FOLDER = cfg["folder"];
                    }
                } catch { }
            }
        }

        private async void CheckUpdates()
        {
            try
            {
                Log("Starting update check...");
                StatusLabel.Text = "Connecting to server...";
                using var client = new HttpClient();
                
                // Add cache-busting timestamp to avoid GitHub Raw cache
                string json = await client.GetStringAsync(BASE_URL + "patch.json?t=" + DateTime.Now.Ticks);
                Log("Manifest downloaded.");
                
                var remoteFiles = JsonConvert.DeserializeObject<List<PatchFile>>(json);
                if (remoteFiles == null) throw new Exception("Failed to parse manifest.");

                StatusLabel.Text = "Verifying files...";
                _filesToUpdate.Clear();

                foreach (var file in remoteFiles)
                {
                    if (NeedsUpdate(file))
                    {
                        _filesToUpdate.Add(file);
                        Log($"Update needed: {file.Path}");
                    }
                }

                if (_filesToUpdate.Count > 0)
                {
                    StatusLabel.Text = $"Updating ({_filesToUpdate.Count} files)...";
                    await DownloadFiles();
                }
                else
                {
                    Log("All files are up to date.");
                }

                StatusLabel.Text = "Meraki is ready!";
                UpdateProgress.Value = 100;
                StartBtn.IsEnabled = true;
            }
            catch (Exception ex)
            {
                Log("ERROR: " + ex.ToString());
                MessageBox.Show("Error checking updates: " + ex.Message);
                StatusLabel.Text = "Offline Mode - Ready";
                StartBtn.IsEnabled = true;
            }
        }

        private void Log(string message)
        {
            try {
                File.AppendAllText("launcher_log.txt", $"[{DateTime.Now:HH:mm:ss}] {message}\n");
            } catch { }
        }

        private bool NeedsUpdate(PatchFile file)
        {
            if (!File.Exists(file.Path)) return true;
            using var md5 = MD5.Create();
            using var stream = File.OpenRead(file.Path);
            byte[] hash = md5.ComputeHash(stream);
            string localMd5 = BitConverter.ToString(hash).Replace("-", "").ToLowerInvariant();
            return localMd5 != file.Md5.ToLowerInvariant();
        }

        private async Task DownloadFiles()
        {
            using var client = new HttpClient();
            int count = 0;
            foreach (var file in _filesToUpdate)
            {
                Log($"Downloading: {file.Path}");
                StatusLabel.Text = $"Downloading {Path.GetFileName(file.Path)}...";
                Directory.CreateDirectory(Path.GetDirectoryName(file.Path) ?? ".");
                
                var bytes = await client.GetByteArrayAsync(BASE_URL + "files/" + file.Path.Replace("\\", "/"));
                await File.WriteAllBytesAsync(file.Path, bytes);
                
                count++;
                UpdateProgress.Value = (double)count / _filesToUpdate.Count * 100;
            }
            Log("All downloads completed.");
        }

        private void StartBtn_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                string l2Path = Path.Combine("system", "L2.exe");
                if (File.Exists(l2Path))
                {
                    Process.Start(new ProcessStartInfo(l2Path) { UseShellExecute = true });
                    Application.Current.Shutdown();
                }
                else
                {
                    MessageBox.Show("L2.exe not found in system folder!");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Failed to launch game: " + ex.Message);
            }
        }

        private void CloseBtn_Click(object sender, RoutedEventArgs e) => Application.Current.Shutdown();

        public class PatchFile
        {
            public string Path { get; set; } = "";
            public string Md5 { get; set; } = "";
            public long Size { get; set; }
        }
    }
}
