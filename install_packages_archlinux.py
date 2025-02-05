import subprocess

def run_command(command):
    try:
        print(f"Executing: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")

commands = [
    "sudo pacman -Sy --noconfirm",
    "sudo pacman -Su --noconfirm",
    "sudo pacman -S --noconfirm yay",
    "yay -S --noconfirm debugedit",
    "yay -S --noconfirm base-devel",
    "yay -S --noconfirm bluez",
    "yay -S --noconfirm bluez-utils",
    "yay -S --noconfirm blueman",
    "sudo systemctl start bluetooth.service",
    "sudo systemctl enable bluetooth.service",
    "yay -S --noconfirm sublime-text",
    "yay -S --noconfirm visual-studio-code-bin",
    "yay -S --noconfirm keepassxc",
    "yay -S --noconfirm localsend-bin",
    "yay -S --noconfirm python-pip",
    "yay -S --noconfirm python-virtualenv",
    "yay -S --noconfirm python-fastapi",
    "yay -S --noconfirm uvicorn",
    "yay -S --noconfirm postman",
    "yay -S --noconfirm android-studio",
    "yay -S --noconfirm snapd",
    "sudo systemctl enable --now snapd.socket",
    "sudo systemctl enable --now snapd.apparmor.service",
    "sudo ln -s /var/lib/snapd/snap /snap",
    "sudo snap install chatgpt-desktop",
    "sudo snap install notion-snap-reborn",
    "sudo snap install trello-desktop",
    "sudo snap install whatsapp-linux-app",
    "sudo snap install deepseek-desktop"
    "yay -S --noconfirm flatpak",
    "yay -S --noconfirm npm",
    "yay -S --noconfirm pnpm",
    "yay -S --noconfirm docker",
    "yay -S --noconfirm docker-compose",
    "sudo groupadd docker",
    "sudo usermod -aG docker $USER",
    "sudo systemctl enable docker.service",
    "sudo systemctl enable containerd.service",
    "yay -S --noconfirm google-chrome",
    "yay -S --noconfirm firefox",
    "yay -S --noconfirm opera",
    "yay -S --noconfirm spotify",
    "yay -S --noconfirm slack-desktop",
    "yay -S --noconfirm ttf-jetbrains-mono-git",
    "yay -S --noconfirm ttf-jetbrains-mono-nerd",
    "curl -f https://zed.dev/install.sh | sh",
    "echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc",
    "source ~/.bashrc",
    "yay -S --noconfirm nginx",
    "yay -S --noconfirm openssh",
    "yay -S --noconfirm nano",
    "yay -S --noconfirm exa",
    "yay -S --noconfirm networkmanager-openvpn",
    "yay -S --noconfirm openvpn",
    "yay -S --noconfirm spectacle",
    "sudo pacman -S --noconfirm jdk17-openjdk",
    "yay -S --noconfirm cmake",
    "yay -S --noconfirm automake",
    "yay -S --noconfirm ninja",
    "yay -S --noconfirm clang",
    "curl -fsSL https://ollama.com/install.sh | sh"
    "flatpak install -y flathub org.libreoffice.LibreOffice",
    "flatpak install -y flathub io.github.thetumultuousunicornofdarkness.cpu-x",
    "flatpak install -y flathub com.github.jeromerobert.pdfarranger",
    "yay -S --noconfirm lutris",
    "yay -S --noconfirm wine wine-mono wine-gecko",
    "mkdir -p ~/Projects",
    "mkdir -p ~/development",
    "git config --global user.name 'victorzarzar'",
    "git config --global user.email 'victor@example.com'",
    "curl -fsSL https://fvm.app/install.sh | bash",
    "yay -S --noconfirm sqlite",
    "yay -S --noconfirm starship",
    "yay -S --noconfirm zsh-autosuggestions"
]

for cmd in commands:
    run_command(cmd)
