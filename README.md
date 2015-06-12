SSD Linker
==========

Note: code is not yet implemeted, so just posting the idea with faith I will impelent it in near future...

SSD Linker is two way symlinks manager. It helps to move files from HDD to SSD (to speed up) and from SSD to HDD (to safe SSD lifecycles). For both cases it creates symlinks after moving files to keep this move invisible for all applications.

So SSD Linker is a GUI tool for easy managing cross-drive (ssd and hdd) links. And it is suitable for next applications:

0. Using SSD as a cache for set of folders from HDD to speed up gaming/apps;

Creates symlinks from HDD to SSD drive. Example:

* C:\ is SSD
* D:\ is HDD

And you want to speed up game at D:\games\GTAVI  (~50GB). SSD Linker will:

* copy content to C:\__ssd_linker_storage__\d\games\GTAVI
* optionally move original dir to backup D:\__ssd_linker_backup__\games\GTAVI to save time on unlinking (but do not free space during linked stage);
* or just delete original dir D:\games\GTAVI (save space, but will require copying data back on unlinking)

Once you are done with particular game you might unlink it, so it will move data back to original driver and delete symlinks.

If you don’t have enough space on SSD to store all game you can symlink only selected folders or even files. For example you have 30 GB free on SSD and game is 50GB. So you go inside D:\games\GTAVI and see:

* data_1 - 5 GB
* data_2 - 35 GB
* data_3 - 10 GB

You can move data_1 and data_3, so 5 + 10 = 15 GB will be used, or go deeper inside data_2 and select any amount of files/folders to fill your free space.
But don’t try to use all your available space on system disk(C:\), because windows will not be quite happy if no space left on system device. I would recomment to have at least 5 to 10 Gb free on system drive.

0. Using SSD Linker to move data out of SSD to HDD.

When you install Windows on SSD you may want to move some files from system disk to HDD:
move all caches and frequently changed files to HDD to save SSD life cycles;
move big files to HDD to free up space and use it for something more usefull(games?);
