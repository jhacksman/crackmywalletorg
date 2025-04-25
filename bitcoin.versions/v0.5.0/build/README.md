# Bitcoin v0.5.0 Headless Client Build

This directory contains a pre-built Bitcoin v0.5.0 headless client (bitcoind) compiled from the original source code without any modifications.

## Build Information

- **Bitcoin Version**: v0.5.0
- **Build Date**: April 25, 2025
- **Build Environment**: Ubuntu 12.04 (Docker container)
- **Architecture**: x86-64
- **Type**: Headless client (no GUI)

## Dependencies Used

The following dependencies were used to build this binary, matching the exact versions specified in the original Bitcoin v0.5.0 documentation:

- **GCC**: 4.3.3
- **OpenSSL**: 0.9.8g
- **Berkeley DB**: 4.8.30.NC
- **Boost**: 1.37

## Build Process

1. **Environment Setup**: Used Ubuntu 12.04 Docker container to provide a 2011-era build environment
2. **Berkeley DB Build**: Compiled Berkeley DB 4.8.30.NC from source as it wasn't available in repositories
3. **Bitcoin Compilation**: Built Bitcoin v0.5.0 using the original makefile with the following command:
   ```
   make -f makefile.unix USE_UPNP= BDB_INCLUDE_PATH=/usr/local/BerkeleyDB.4.8/include BDB_LIB_PATH=/usr/local/BerkeleyDB.4.8/lib LDFLAGS="-L/usr/local/BerkeleyDB.4.8/lib"
   ```

## Running the Binary

To run this binary, you need to set the library path for Berkeley DB:

```bash
export LD_LIBRARY_PATH=/usr/local/BerkeleyDB.4.8/lib:$LD_LIBRARY_PATH
./bitcoind
```

Note: You'll need to create a bitcoin.conf file with an rpcpassword to run the daemon.

## Verification

The binary was built without any source code modifications, preserving the original Bitcoin v0.5.0 functionality. The build process followed the exact instructions from the original build-unix.txt documentation.

## Source Code

The source code used for this build can be found in the parent directory: `../bitcoin-bitcoin-f5649b6/`
