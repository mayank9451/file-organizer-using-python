# File Organizer

I made this script because my Downloads folder was a complete mess. Every time I downloaded something, it just piled up there until I had hundreds of files with no organization whatsoever. This script automatically sorts everything into proper folders based on file type.

---

## What This Does

This Python script looks at all the files in a folder and moves them into categorized subfolders. Images go into an Images folder, videos into Videos, documents into Documents, and so on. Files that don't match any category get moved to an Others folder.

By default, it organizes the folder where the script itself is located. So you can just drop it into your Downloads folder, run it, and watch everything get sorted automatically.

---

## Requirements

You need Python installed. That's really it. The script uses only standard library modules - os, shutil, and pathlib - so you don't need to install anything extra.

Check if you have Python by running:

```
python --version
```

If you see a version number, you're good.

---

## How to Use It

1. Save the code to a file called `organizer.py`
2. Place it in the folder you want to organize (like your Downloads folder)
3. Run it:

```
python organizer.py
```

Watch the terminal as it moves each file and tells you where it went. When it's done, you'll see a summary of how many files were sorted.

---

## File Types It Handles

The script recognizes these categories:

- **Images** - jpg, jpeg, png, gif, bmp, webp, svg, ico
- **Videos** - mp4, mov, avi, mkv, webm, flv, wmv
- **Documents** - pdf, doc, docx, txt, xls, xlsx, ppt, pptx, csv
- **Audio** - mp3, wav, aac, flac, m4a, wma
- **Archives** - zip, rar, 7z, tar, gz
- **Code** - py, js, html, css, java, cpp, c, sh
- **Others** - Anything that doesn't match the above

---

## Organizing a Different Folder

By default, the script uses the current working directory. If you want to organize a specific folder like your Downloads, find this line in the script:

```python
SOURCE_DIR = os.getcwd()
```

And change it to:

```python
SOURCE_DIR = "C:/Users/YourName/Downloads"
```

On Windows, use forward slashes in the path even though Windows typically uses backslashes. It avoids some headaches with escape characters.

---

## Adding New File Types

Let's say you want to add a category for Photoshop files. Edit the FILE_TYPES dictionary and add:

```python
'Photoshop': ['.psd', '.psb'],
```

Just make sure you follow the same format - the category name as the key, and a list of extensions as the value.

---

## What Happens to Existing Folders

The script only moves files, not folders. So if you already have some organization in place with your own subfolders, those won't be touched. It only looks at loose files in the main directory.

Also, if a file with the same name already exists in the destination folder, the script will throw an error. I kept it simple like this because handling duplicates gets complicated fast. If you need that feature, you'd have to add some logic to rename files or skip them.

---

## Why I Built This

I got tired of manually sorting files every few weeks. I tried other solutions, but most of them were either too complicated or wanted to install background services. I just wanted something I could run whenever I wanted and forget about.

This script does exactly that. It's not fancy, it doesn't have a GUI, but it works reliably. I run it once a month or so and my Downloads folder stays clean.

---

## Safety Tips

Before running this on an important folder for the first time, I'd recommend testing it on a dummy folder. Make a test folder with some random files, run the script, and make sure it does what you expect.

Also, if you're organizing a folder that gets new files frequently, you might want to run this on a schedule. On Windows, you can use Task Scheduler. On Mac or Linux, you can set up a cron job. But honestly, I just run mine manually when I remember.

---

## Things That Could Be Better

I'll be honest, this is a pretty basic implementation. Here are some things I thought about adding but didn't:

- A way to undo the organization if something goes wrong
- Automatic scheduling to run every week
- A GUI for people who don't like the command line
- Duplicate file handling

Maybe I'll add those someday, but for now this solves my problem and I didn't want to overcomplicate it.

---

## License

Free to use, modify, whatever. If it helps you keep your files organized, that's the point.