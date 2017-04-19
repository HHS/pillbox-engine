With Pillbox Engine, you can easily download SPL files from DailyMed and unzip them.

## SPL Sources

DailyMed has five sources of SPL data. These five sources are included in the Pillbox Engine under Sources table.

![Sources](../img/sources.png?raw=true)

The sources are:

- Human Prescription Labels (HRX) - 3 files
- Human OTC Labels (HOTC) - 3 files
- Homeopathic Labels (HOMEO) - 1 file
- Animal Labels (ANIMAL) - 1 file
- Remainder Labels (REMAIN) - 1 file

These files are stored as zip on NLM ftp servers. Links to the files are [listed here](http://dailymed.nlm.nih.gov/dailymed/spl-resources-all-drug-labels.cfm).

## Download and Unzip

Pillbox Engine includes a ftp client that download all files and keep track of the download progress. When the files are downloaded, the Engine unzip them, copy all the xml files inlcuded in each zip file into a designated folder and delete the remaining data.

Each zip file is fairly large (around 3gb). The download and unzip process for each SPL source could take 1 to 2 hours depending on your internet speed.

The zipped and unzipped files are stored in your pillbox engine installation folder.

- Unzip path: `pillbox-engine/downloads/unzip`
- Zip path: `pillbox-engine/downloads/zip`

The zip and unzip folders requires large storage space. In average, both folders require at least 42 GB of storage.

Whenever you start a download, the ftp client checks the files on the FTP server to make sure they are newer than the existing files before starting the download process. If the files on remote FTP server are not newer, the Pillbox Engine skips the download and only unzip the already existing files.

You can keep track of all the downloaded files by visiting [the sources page](http://localhost:5000/spl/source/). If you click on a particular source, you can find more information about the source such as the number of xml files the source include, the name ftp server address and the name of the file that has to be downloaded.

![Animal Source](../img/animal_source.png?raw=true)
