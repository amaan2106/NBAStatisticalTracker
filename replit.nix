{ pkgs }: {
  deps = [
    pkgs.glibcLocales
    pkgs.gdb
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
  ];
}