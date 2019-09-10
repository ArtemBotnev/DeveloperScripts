## fast backup script
### backup.sh
 Requires python version 3.5 or higher.
 
 Copies all new and updated source directory files to destination directory
 (checks if each file already exist in destination directory and copy only if
 it doesn't or has been updated).
 
 Copies full directories tree.
 
 Exclude empty folders.
 
#### *Usage example:*
copy data from ```~/source``` directory to ```~/dist``` directory
```sh
./backup.sh ~/source ~/dist
