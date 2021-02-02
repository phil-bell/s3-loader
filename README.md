# `s3-loader`

**Install**
```console
pip install s3-loader
```

**Usage**:

```console
$ s3-loader [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `auth`: to set aws credetials
* `empty-bucket`: delete everything in an s3 bucket
* `upload-dir`: upload an entire directory to s3
* `upload-file`: upload a single file to s3

## `s3-loader auth`

to set aws credetials

**Usage**:

```console
$ s3-loader auth [OPTIONS]
```

**Options**:

* `--aws-access-key-id TEXT`: Your aws access key  [required]
* `--aws-secret-access-key TEXT`: Your aws secret acess key  [required]
* `--help`: Show this message and exit.

## `s3-loader empty-bucket`

delete everything in an s3 bucket

**Usage**:

```console
$ s3-loader empty-bucket [OPTIONS]
```

**Options**:

* `--bucket-name TEXT`: Your bucket name  [required]
* `--help`: Show this message and exit.

## `s3-loader upload-dir`

upload an entire directory to s3

**Usage**:

```console
$ s3-loader upload-dir [OPTIONS]
```

**Options**:

* `--path TEXT`: Path to your directory  [required]
* `--bucket-name TEXT`: Your bucket name  [required]
* `--help`: Show this message and exit.

## `s3-loader upload-file`

upload a single file to s3

**Usage**:

```console
$ s3-loader upload-file [OPTIONS]
```

**Options**:

* `--local-file TEXT`: Local file name  [required]
* `--bucket TEXT`: Your bucket name  [required]
* `--s3-file TEXT`: Name the file will use on s3  [required]
* `--help`: Show this message and exit.
