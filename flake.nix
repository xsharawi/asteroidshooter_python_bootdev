{
  description = "pygame dev shell (SDL + Wayland/X11 + uv)";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    system = "x86_64-linux";
    pkgs = import nixpkgs {inherit system;};
    python = pkgs.python313;
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        # Python + tools
        python
        python313Packages.pygame
        uv
        bootdev-cli

        # SDL core
        SDL2
        SDL2_image
        SDL2_mixer
        SDL2_ttf

        # Wayland
        wayland
        wayland-protocols
        libxkbcommon

        # X11 (XWayland fallback – REQUIRED on Hyprland)
        xorg.libX11
        xorg.libXcursor
        xorg.libXrandr
        xorg.libXi
        xorg.libXinerama

        # Graphics stack
        mesa
        libGL
        libdrm

        # Debug helpers (optional but useful)
        strace
        lsof
      ];

      shellHook = ''
        echo "🐍 pygame dev shell ready"
        echo "Python: $(python --version)"

        # Force sane defaults for Hyprland
        export SDL_VIDEODRIVER=x11
        export SDL_AUDIODRIVER=pulseaudio
        export SDL_RENDER_DRIVER=software

        # Avoid offscreen fallback
        unset SDL_VIDEODRIVER_WAYLAND

        # Useful for debugging if something breaks again
        # export SDL_DEBUG=1
      '';
    };
  };
}
