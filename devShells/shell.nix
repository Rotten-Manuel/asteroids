{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = with pkgs; [
    uv
    (python3.withPackages(pypkgs: with pypkgs; [
      pygame
      black
    ]))
  ];
}
