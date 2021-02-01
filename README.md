# `s3-uploader`

**Usage**:

```console
$ s3-uploader [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `auth`
* `clear-bucket`
* `upload-dir`
* `upload-file`

## `s3-uploader auth`

**Usage**:

```console
$ s3-uploader auth [OPTIONS] AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY
```

**Arguments**:

* `AWS_ACCESS_KEY_ID`: [required]
* `AWS_SECRET_ACCESS_KEY`: [required]

**Options**:

* `--help`: Show this message and exit.

## `s3-uploader clear-bucket`

**Usage**:

```console
$ s3-uploader clear-bucket [OPTIONS] BUCKETNAME
```

**Arguments**:

* `BUCKETNAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `s3-uploader upload-dir`

**Usage**:

```console
$ s3-uploader upload-dir [OPTIONS] PATH BUCKETNAME
```

**Arguments**:

* `PATH`: [required]
* `BUCKETNAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `s3-uploader upload-file`

**Usage**:

```console
$ s3-uploader upload-file [OPTIONS] LOCAL_FILE BUCKET S3_FILE
```

**Arguments**:

* `LOCAL_FILE`: [required]
* `BUCKET`: [required]
* `S3_FILE`: [required]

**Options**:

* `--help`: Show this message and exit.
