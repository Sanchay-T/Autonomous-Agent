Skip to main content

Claim your spot on the [waitlist](https://paperspace-6894371.hs-
sites.com/paperspace-h100) for the NVIDIA H100 GPUs!

[![Paperspace Docs](https://docs.paperspace.com/img/logo-light-theme.svg)
**DOCS**](https://docs.paperspace.com/)[Notebooks](https://docs.paperspace.com/gradient/notebooks/)[Machines](https://docs.paperspace.com/core/)[Deployments](https://docs.paperspace.com/gradient/deployments/)[Account](https://docs.paperspace.com/account-management/)

`ctrl``K`

[![](https://docs.paperspace.com/img/icon-account.svg)Account](https://docs.paperspace.com/account-management)

[Sign in](https://console.paperspace.com/)[Sign
up](https://console.paperspace.com/signup)

[![Paperspace Docs](https://docs.paperspace.com/img/logo-light-theme.svg) **DOCS**](https://docs.paperspace.com/)

  * [Notebooks](https://docs.paperspace.com/gradient/notebooks/)
  * [Machines](https://docs.paperspace.com/core/)
  * [Deployments](https://docs.paperspace.com/gradient/deployments/)
  * [Account](https://docs.paperspace.com/account-management/)

← Back to main menu

  * Getting Started

  * Gradient Platform

    * Notebooks

      * [Overview](https://docs.paperspace.com/gradient/notebooks/)
      * [Runtimes](https://docs.paperspace.com/gradient/notebooks/runtimes)
      * [Storage and datasets](https://docs.paperspace.com/gradient/notebooks/notebook-storage)
      * [Machines](https://docs.paperspace.com/gradient/notebooks/machines)
      * [Terminal](https://docs.paperspace.com/gradient/notebooks/terminal)
      * [Remote Jupyter Kernel](https://docs.paperspace.com/gradient/notebooks/notebooks-remote-kernel)
      * [Sharing](https://docs.paperspace.com/gradient/notebooks/sharing)
      * [TensorBoard](https://docs.paperspace.com/gradient/notebooks/tensorboard)
    * Workflows [beta]

    * Deployments

  * Gradient Resources

  * CLI & SDK

  * [🚀 Run on Gradient](https://docs.paperspace.com/gradient/notebooks/run-on-gradient)

[{/**/}Account](https://docs.paperspace.com/account-management)

[{/**/}Changelog](https://updates.paperspace.com)

[Contact Support](https://docs.paperspace.com/contact-support)

  * [](https://docs.paperspace.com/)
  * Gradient Platform
  * Notebooks
  * Storage and datasets

On this page

# Storage and datasets

In Gradient Notebooks, there is a file browser, shared persistent storage, and
Gradient Datasets. This guide explains the full storage architecture of your
notebook.

## Introduction to the file architecture of Gradient Notebooks​

Every notebook in Gradient has a file management interface that looks like
this:

![The file manager for Gradient Notebooks lives in the left
sidebar.](https://docs.paperspace.com/assets/images/notebook-started-0a00613ac3f409b6616be8aad98b879a.png)

The file manager within the notebook does **not** represent the full file
structure of the notebook.

The full file structure of a notebook is as follows:

![This is the full representation of the file structure behind Gradient
Notebooks. Notice that the file manager in Gradient Notebooks is represented
by the yellow box titled { notebook IDE }.](https://docs.paperspace.com/assets/images/local-file-architecture-710291ebcbbec2ce6c2268447def4c06.png)

Here are the main components:

  *  **File manager** \- Files available in the normal IDE sidebar. This corresponds to the directory located at `/notebooks`.
  *  **Storage** \- Shared persistent storage directory accessible to your entire team on a specific cluster. Available at `/storage`. This is a method for sharing data across notebooks and users. In the case of the **Private Workspace** team, the `/storage` volume cannot be shared with other users.
  *  **Gradient Datasets** \- Team and public datasets that you can mount in the IDE. Ideal for large amounts of data and for sharing. Public datasets include popular datasets that Gradient makes available out of the box such as [MNIST](http://yann.lecun.com/exdb/mnist/).

## What is the file manager?​

Refer to Introduction to the file structure of Gradient Notebooks to
understand the overall file architecture of Gradient Notebooks.

Files stored in the file manager are persisted across notebook sessions. This
is the same directory that is represented by the yellow box labeled `{
notebook IDE }` in the previous section.

caution

Within the `/notebooks` directory, the folder name `checkpoints` is reserved
by Jupyter. Avoid using `checkpoints` as a directory name in order to avoid
any unexpected behavior.

![Files in the notebook IDE file manager \(pictured on the left side of the
image\) are available whenever a notebook is in the Running
state.](https://docs.paperspace.com/assets/images/notebook-file-manager-4823ac255cc2e3a05c97897653833f80.png)

The notebook must be in the **Running** state to display files.

### How to upload large files and folders to the file manager​

To upload a large number of files or a large amount of data, it is best to use
command-line libraries such as [curl](https://curl.se),
[Wget](https://www.gnu.org/software/wget/), or
[gdown](https://github.com/wkentaro/gdown).

Here is an example of how to use Wget to download the [Stanford Dogs
dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/) to our notebook:

![An easy way to download a large dataset to a notebook is to use the wget
command.](https://docs.paperspace.com/assets/images/stanford-dogs-121f8efedac73ef8a7ce19c7cbb56e51.gif)

This command downloads the dataset to our current folder:

    
    
    !wget http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar  
    

That's all there is to it! We can also perform the same command from the
terminal if we are on the Pro or Growth subscription plans.

#### Transferring files from Google Drive​

Files/folders in Google Drive can be brought into your notebook using `gdown`.

  1. Through the notebook or terminal execute: `pip install gdown` to install and `pip install --upgrade gdown` to upgrade. Use a `!` before each command in the notebook.
  2. In the permissions settings of the files/folders you want to upload, set the permissions to “Anyone with the Link.”
  3. Obtain the `file id` by copying and extracting it from the file share link and use the following commands based on your needs.

![Obtain the file id in the Google Drive share
link.](https://docs.paperspace.com/assets/images/googledrivelink-abc4772e91de38173d9b63c929c90052.png)

  * For bigger than 500 Mb files use: `gdown "<file_ID>&confirm=t"`
  * For smaller files `gdown <file_ID>`
  * For Folders `gdown https://drive.google.com/drive/folders/<file_ID> -O /tmp/folder --folder`

### How to download files and folders to the file manager​

To download large files or folders from the notebook, we suggest you zip/tar
the files first. You can do this from the notebook or terminal.

  1. Compress the files/folders using the following command in a notebook code cell or the terminal. If you use the notebook make sure to add a `!` before each command.

    1. tar
        
                cd /notebooks  
        tar -cf [filename].tar [file1] [file2]...  
        

    2. zip
        
                cd /notebooks  
        zip -r [filename].zip [file1] [file2]...  
        

  2. Refresh the file manager

  3. Right click on the compressed file created

  4. Select the option **Download**

If the files are in shared storage or a dataset, they can be downloaded by
moving them into the file manager and following the steps shown above.

## What is shared storage?​

Refer to Introduction to the file structure of Gradient Notebooks to
understand the overall file architecture of Gradient Notebooks.

Data can be shared between users on a team and between notebooks that belong
to users on a team.

Access to shared persistent storage must be done through code, either via the
notebook terminal or via a code cell within a notebook, as there is currently
no way to access shared persistent storage from the GUI.

note

Shared storage cannot be accessed cross cluster. As a result, data stored in
`/storage` on the Gradient cluster will not be accessible on the Graphcore
cluster.

### How to access shared persistent storage from a notebook code cell​

We can access shared persistent storage from a code cell within a notebook
using the `!` operator and issuing our bash commands on a single line
connected with the `&&` operator.

For example, to create a new directory within our persistent `/storage`
directory, we'll input the following:

    
    
    !cd /storage && mkdir data && cd data  
    

This is what that would look like in a notebook code cell:

![Access shared persistent storage using the ! operator and entering bash
commands on a single line with the &amp;&amp; operator.](https://docs.paperspace.com/assets/images/slash-storage-44e5eb2a54ca33f3aa0e5ce342d8c256.gif)

We can also access persistent storage via the terminal, as described in the
next section.

### How to access shared persistent storage from a notebook terminal​

The terminal feature requires Gradient Pro or Gradient Growth subscriptions.

To access persistent storage in a Gradient Notebooks terminal, we can use the
`cd` command to change into the persistent directory `/storage`.

Let's say we'd like to create a new persistent directory called `data`. We can
accomplish this as follows:

    
    
    cd /storage  
    mkdir data  
    cd data  
    

Let's try it out:

![Here we use the terminal to create a new shared persistent storage directory
located at /storage/data.](https://docs.paperspace.com/assets/images/terminal-storage-759f79b1c3726e9cc729fd283abd3456.gif)

We can now use the directory located at `/storage/data` to store any files we
need to access across users and notebooks.

### How to view storage limits​

Storage in Gradient is scoped to the team level. By default, storage tiers are
as follows:

| Free| Pro| Growth| Enterprise  
---|---|---|---|---  
Storage| 5 GB| 15 GB| 50 GB| ∞ GB  
  
Excess storage is billed at $0.29 per GB per month and this is prorated for
the duration of the month.

As an example, if we are on the Pro plan, which grants us 15 GB of storage,
and we use 50 GB of storage for an entire month, we will be billed (50 - 15) *
0.29 = $10.15 on top of our normal bill.

To view storage utilization, visit the **Storage** tab in the workspace
settings.

Here we have an example of the **Storage** tab for a new team that is not yet
using any volume storage:

![A new team that has yet to upload data will have nothing to display in the
Storage tab in team settings.](https://docs.paperspace.com/assets/images/empty-storage-example-80ea2bc7b391fd35d607f4cd2c181faa.png)

Here we have an example of a Private Workspace team that is using a good
amount of storage:

![A team that has uploaded data will see a summary of storage volumes in the
Storage tab.](https://docs.paperspace.com/assets/images/storage-example-8e7fefc63f426be5edbff0638d0a70f0.png)

If we expect to be billed for storage overages, we can use the **Utilization**
tab to explore our storage use further.

Use the file management tab to upload data, organize files and folders, and
download files stored in a notebook.

Some additional options such as renaming, duplicating, and deleting files and
folders are available by clicking the menu icon on the individual entity.

![A number of file and folder management options are available in the Files
sidebar.](https://docs.paperspace.com/assets/images/file-management-options-ba85cc0d826fbc5a44fb0f415b0dcb92.png)

There are multiple ways to upload files to a notebook, which are discussed in
the following sections.

## What is a dataset?​

Refer to Introduction to the file structure of Gradient Notebooks to
understand the overall file architecture of Gradient Notebooks.

Gradient Datasets are available as a first-class resource within Gradient
Notebooks.

### How to mount datasets in a notebook​

The IDE supports mounting Gradient Datasets to explore data and train models.
Use the datasets tab to mount existing team datasets, mount public datasets,
and create new team datasets.

Mounting a dataset is as easy as clicking the MOUNT button next to either the
team or public dataset you would like to use.

![Mount a public dataset](https://docs.paperspace.com/assets/images/mount-public-dataset-5ad4d25bca8844329aad46f78f033f94.gif)

When mounting a team dataset, this will only mount the `latest` version of a
dataset. To change the version of the dataset please see the Advanced Settings
section below.

## How to add small datasets to a notebook​

To add a new dataset, click on the + icon. Then name, describe and upload the
data. Feel free to close the modal once you start the upload, this process is
still happening in the background.

![Upload some images from Stanford Dogs dataset](https://docs.paperspace.com/assets/images/uploading-files-to-dataset-b69a1d40e1981eb19b98c5abcc281442.gif)

Datasets can also be added from the Gradient Project level. To learn more see
[this article](https://docs.paperspace.com/gradient/data/#how-to-create-a-dataset-and-dataset-version-in-the-cli).

### How to add large datasets (5GB +) to a notebook​

To create datasets larger than 5GB, you can use the CLI through the terminal.
To learn more about how to create a dataset through the CLI see [this
article](https://docs.paperspace.com/gradient/data/#how-to-create-a-dataset-and-dataset-version-in-the-cli)

### Datasets Advanced Settings​

To access the settings file that manages all of your mounted Datasets go to
`.gradient/settings.yaml`. Here you can see all of the mounted Datasets and
their arguments. This file should only be used to do one of the following:

  1. Change the `version-id` of the dataset that should be mounted.

    
    
    integrations:  
      quarterly-reports: # mounts in /datasets/quarterly-reports  
        type: dataset # denotes a paperspace dataset  
        id: dataset-id # a paperspace dataset id  
        version: verion-id # a paperspace version id  
      my-bucket-data: # mounts in /datasets/my-bucket-data  
        type: s3 # an s3 bucket  
        url: s3://my-bucket/my-data # your s3 bucket url  
        accessKeyId: AK123 # your s3 access key id  
        secretAccessKey: secret:my-bucket-secret-key # a paperspace secret with your s3 secret key  
        region: "us-west-1" # the aws region your bucket is in, if not in aws set "endpoint"  
        endpoint: "https://my-bucket-host.com" # a custom bucket host, do not set region if set  
    

## Other Data Sources​

### DigitalOcean Spaces​

The Gradient IDE provides the ability to mount DigitalOcean Spaces into
Notebooks to access data that is stored externally. This is available to Pro
and Growth plans. Follow these simple steps to mount your DigitalOcean Space.

  1. Add a new data source and select the DigitalOcean Spaces icon.
  2. Enter the endpoint url (e.g. `https://jane.nyc3.digitaloceanspaces.com`), display name (an arbitrary name for the data source), along with the access key & secret.
    * note: you will have to upload project secrets to the under the project settings tab.

![DigitalOcean Spaces data source](https://docs.paperspace.com/assets/images/do-data-source-b78516e544a1e4bedaf50b819a361eed.png)

Once the data source is created, find the source in the list of data sources
and click the mount button.

This will create a bidrectional mount on the underlying container for reading
and writing data to the space.

### AWS S3​

The Gradient IDE provides the ability to mount public and private S3 buckets
into the Notebook to access data that is stored externally. This is available
to Pro and Growth plans. Follow these simple steps to mount your S3.

  1. Add a new data source and select the Amazon S3 icon.
  2. Enter the name of your datasource and bucket url. 
  3. If the bucket is private add an Access Key ID and Secret Access Key by choosing a Gradient Secret in the dropdown. [Learn more](https://docs.paperspace.com/gradient/secrets/) about how to create a Gradient secret. 
  4. The data source can now be mounted to your notebook and accessed through the data source panel.

![This is how you mount an AWS S3 data source into the
IDE](https://docs.paperspace.com/assets/images/s3-data-source-mount-8490fb3e309a91bfe76a125cd2bc17d7.gif)

