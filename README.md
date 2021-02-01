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

* `auth`: authenticate with your aws access key and...
* `clear-bucket`: delete everything in an s3 bucket
* `upload-dir`: upload an entire directory to s3
* `upload-file`: upload a single file to s3

## `s3-loader auth`

authenticate with your aws access key and secret

**Usage**:

```console
$ s3-loader auth [OPTIONS] [AWS_ACCESS_KEY_ID] [AWS_SECRET_ACCESS_KEY]
```

**Arguments**:

* `[AWS_ACCESS_KEY_ID]`: Your aws access key  [default: ]
* `[AWS_SECRET_ACCESS_KEY]`: Your aws secret acess ket  [default: ]

**Options**:

* `--help`: Show this message and exit.

## `s3-loader clear-bucket`

delete everything in an s3 bucket

**Usage**:

```console
$ s3-loader clear-bucket [OPTIONS] [BUCKET_NAME]
```

**Arguments**:

* `[BUCKET_NAME]`: Your bucket name  [default: ]

**Options**:

* `--help`: Show this message and exit.

## `s3-loader upload-dir`

upload an entire directory to s3

**Usage**:

```console
$ s3-loader upload-dir [OPTIONS] [PATH] [BUCKET_NAME]
```

**Arguments**:

* `[PATH]`: Path to your directory  [default: ]
* `[BUCKET_NAME]`: Your bucket name  [default: ]

**Options**:

* `--help`: Show this message and exit.

## `s3-loader upload-file`

upload a single file to s3

**Usage**:

```console
$ s3-loader upload-file [OPTIONS] [LOCAL_FILE] [BUCKET] [S3_FILE]
```

**Arguments**:

* `[LOCAL_FILE]`: Local file name  [default: ]
* `[BUCKET]`: Your bucket name  [default: ]
* `[S3_FILE]`: Name the file will use on s3  [default: ]

**Options**:

* `--help`: Show this message and exit.
