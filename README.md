# fastfetch-touhou-hats
A simple Python script that applies Touhou characters' hats as fastfetch logo.

![example](screenshots/example1.png)

# Installation

```
git clone https://github.com/pwoertnehsi/fastfetch-touhou-hats
```

Additionally, you can add ffth binary to your PATH. To make the change persistent, add the line below to your ~/.bashrc

```
export PATH=$PATH:/path/to/fastfetch-touhou-hats/ffth
```

If you don't want to run the compiled binary, you would need to `pip install json5`

# Usage

run `/path/to/fastfetch-touhou-hats/ffth/ffth` or just `ffth` if you've added the folder to your PATH.

![example](screenshots/example2.png)

Note that once the backup is made, the script will stop attempting to backup your config unless you manually delete ~/.config/fastfetch/config.jsonc.bak  

# Character List

These are the characters whose hats are available. Links are the arts that I've traced the hats from. 

- [Patchouli Knowledge](https://gelbooru.com/index.php?page=post&s=view&id=3442232)
- [Saigyouji Yuyuko](https://www.pixiv.net/en/artworks/138944424)
- [Yakumo Yukari](https://girlcockx.com/y_karas/status/1110231080613740544)
- [Yakumo Ran](https://girlcockx.com/miyama_sos/status/1997801267197088189)

# TODO

- Kurokoma Saki
- Moriya Suwako
- Futatsuiwa Mamizou
- Hong Meiling
- Hakurei Reimu
- Kirisame Marisa
