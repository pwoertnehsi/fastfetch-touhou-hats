# fastfetch-touhou-hats
A simple Python script that applies Touhou characters' hats as fastfetch logo.

![example](https://patchouliknowledge.com/images/git/fastfetch-touhou-hats/example1.png)

# Installation

### Manual

```
git clone https://git.patchouliknowledge.com/tenshi/fastfetch-touhou-hats
```

You would need Python json5 library for this script to work.

### Arch Linux package (makepkg)

```
git clone https://git.patchouliknowledge.com/tenshi/fastfetch-touhou-hats-pkg
cd fastfetch-touhou-hats-pkg
makepkg -si
```

### Arch Linux package (repo)

Add this to your /etc/pacman.conf:
```
[patchouli]
SigLevel = Optional TrustAll                                                     
Server = https://repo.patchouliknowledge.com/archlinux/$repo/os/$arch
```
Then run:
```
sudo pacman -Syu fastfetch-touhou-hats
```

# Usage

Run `./ffth.py` inside the repo or just `ffth` if you've installed this tool as a package

![example](https://patchouliknowledge.com/images/git/fastfetch-touhou-hats/example2.png)

Note that once the backup is made, the script will stop attempting to backup your config unless you manually delete ~/.config/fastfetch/config.jsonc.bak  

# Character List

These are the characters whose hats are available. Links are the arts that I've traced the hats from. 

- [Patchouli Knowledge](https://gelbooru.com/index.php?page=post&s=view&id=3442232)
- [Saigyouji Yuyuko](https://www.pixiv.net/en/artworks/138944424)
- [Yakumo Yukari](https://girlcockx.com/y_karas/status/1110231080613740544)
- [Yakumo Ran](https://girlcockx.com/miyama_sos/status/1997801267197088189)
- [Futatsuiwa Mamizou](https://www.pixiv.net/en/artworks/76054872)
- [Kurokoma Saki](https://www.pixiv.net/en/artworks/120203173)

# TODO

- Moriya Suwako
- Hong Meiling
- Hakurei Reimu
- Kirisame Marisa
