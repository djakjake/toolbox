# **toolbox**

A collection of tools, scripts, functions, files, etc... that can be used for projects.

_toolbox_ was developed and tested with the following system and environment:
- **OS**          : Ubuntu 22.04.3 LTS
- **python**      : Python 3.10.12
- **g++ compiler**: g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

# **directories**

## **bash**

[README.md](https://github.com/djakjake/toolbox/blob/main/bash/README.md)

## **cpp**

[README.md](https://github.com/djakjake/toolbox/blob/main/cpp/README.md)

## **pytools**

[README.md](https://github.com/djakjake/toolbox/blob/main/pytools/README.md)

## **templates**

A collection of template files

- `__main__.py`
- `README.md`

# **Meld**

## **Install**

_Meld_ is a useful tool for diffing files. To install _Meld_ on Ubuntu, you must install [_flatpak_](https://flathub.org/setup/Ubuntu). _flatpak_ can be installed by running:
```bash
bash $DIR_TOOLBOX/bash/install_flatpack.sh
```

To install _Meld_ via flatpak, run:
```bash
flatpak install meld
```

To open _Meld_, run:
```bash
flatpak run org.gnome.meld
```

If you prefer, you can add the line,
```bash
alias meld="flatpak run org.gnome.meld"
```
to your `~/.bashrc`. After you `source ~/.bashrc`, you will be able to open meld using any of the following examples:
```bash
meld                             # open up the meld gui
meld <file 1> <file 2>           # compare 2 files with meld
meld <directory 1> <directory 2> # compare 2 directories with meld
```

All the current _flatpak_ installations can be viewed with:
```bash
flatpak list --app
```

## **Configure _Meld_ for _git_**

To configure _Meld_ to use as your `git difftool`, copy these [lines](https://github.com/flatpak/flatpak/issues/1423#issuecomment-441337743) into your `~/.gitconfig`.
```bash
[diff]
	tool = meld_flatpak

[difftool "meld_flatpak"]
	cmd = flatpak run --file-forwarding org.gnome.meld \"@@\" $LOCAL \"@@\" \"@@\" $REMOTE \"@@\"

[difftool]
	prompt = false
```

To configure _Meld_ to use as your `git mergetool`, copy these [lines](https://stackoverflow.com/questions/34119866/setting-up-and-using-meld-as-your-git-difftool-and-mergetool) into your `~/.gitconfig`.
```bash
[merge]
    tool = meld_flatpak

[mergetool "meld_flatpak"]
    # Choose one of these 2 lines
    #cmd = flatpak run --file-forwarding org.gnome.meld \"@@\" $LOCAL \"@@\" \"@@\" $$BASE \"@@\" \"@@\" $REMOTE \"@@\" --output \"@@\" $MERGED \"@@\"
    cmd = flatpak run --file-forwarding org.gnome.meld \"@@\" $LOCAL \"@@\" \"@@\" $MERGED \"@@\" \"@@\" $REMOTE \"@@\" --output \"@@\" $MERGED \"@@\"
```
