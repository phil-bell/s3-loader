# `s3-loader`

**Usage**:

```console
$ s3-loader [OPTIONS] COMMAND [ARGS]...
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

## `s3-loader auth`

**Usage**:

```console
$ s3-loader auth [OPTIONS] AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY
```

**Arguments**:

* `AWS_ACCESS_KEY_ID`: [required]
* `AWS_SECRET_ACCESS_KEY`: [required]

**Options**:

* `--help`: Show this message and exit.

## `s3-loader clear-bucket`

**Usage**:

```console
$ s3-loader clear-bucket [OPTIONS] BUCKETNAME
```

**Arguments**:

* `BUCKETNAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `s3-loader upload-dir`

**Usage**:

```console
$ s3-loader upload-dir [OPTIONS] PATH BUCKETNAME
```

**Arguments**:

* `PATH`: [required]
* `BUCKETNAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `s3-loader upload-file`

**Usage**:

```console
$ s3-loader upload-file [OPTIONS] LOCAL_FILE BUCKET S3_FILE
```

**Arguments**:

* `LOCAL_FILE`: [required]
* `BUCKET`: [required]
* `S3_FILE`: [required]

**Options**:

* `--help`: Show this message and exit.
