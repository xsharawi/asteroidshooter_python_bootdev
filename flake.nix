{
  description = "nixin my python";

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
        python
        python313Packages.pygame
        uv
        bootdev-cli

        SDL2
        SDL2_image
        SDL2_mixer
        SDL2_ttf

        wayland
        wayland-protocols
        libxkbcommon

        xorg.libX11
        xorg.libXcursor
        xorg.libXrandr
        xorg.libXi
        xorg.libXinerama

        mesa
        libGL
        libdrm

        strace
        lsof
      ];

      shellHook = ''
        echo "🐍 pygame dev shell ready"
        echo "Python: $(python --version)"

        export SDL_VIDEODRIVER=x11
        export SDL_AUDIODRIVER=pulseaudio
        export SDL_RENDER_DRIVER=software

        unset SDL_VIDEODRIVER_WAYLAND
      '';
    };
  };
}
