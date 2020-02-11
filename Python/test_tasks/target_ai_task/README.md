# Async File Transfer

It is necessary to write a client-server application for sending data to the remote machine and further processing.

The application consists of two parts: the client that sends the data and the server that receives, processes and stores the results.

The client is a console utility with which you can specify the path to the data folder and the address of the remote machine using the appropriate flags.

The folder contains a large number (100k+) of small binary files compressed using gzip. The files are named in the following format [a-z]+-\d{7}\.gz. Example file name abc-0000011.gz. Accordingly, the theoretically acceptable number of pieces is 10 million (0000000-99999). These files were obtained by dividing the original large file into equal slices of fixed size and subsequent packing of these slices. In addition, the folder may contain a file marker, in this example abc.done, which indicates that all necessary files in the folder are present and you can start processing them. This file has a single line that contains the size in bytes of the original file, before it is split into pieces and compressed.

When starting, the client checks that the specified folder contains a set of files with names in the format described above and a file marker. If the necessary files are present but there is no file marker, the client waits until the processing is finished and this file appears. If the file is present, you need to start transferring files to the remote machine.

The server part is a service that listens to the port defined by the corresponding flag and waits for data from the client. Also, a separate flag indicates the destination folder. It is necessary to consider that simultaneous clients can be several. The task of the server part is to unzip packed files and collect the original file on disk. The sequence of collected files should correspond to their order number. Besides, it is necessary to create a file marker of the end of work. That is, we have two files at the output: abc and abc.done.

It is necessary to take into account that it is necessary to maximally utilize hardware capabilities of the system (disks, processor cores, network).

To implement it, you should use one of the latest versions of Python 3. It is allowed to use any packages from the standard library, third-party libraries for networking and asynchronous processing. Runtime - OS based on Linux.

The details of the implementation of the communication protocol remain with the executor.

## What is this?
This is async client and server applications which 
transfers files from the client to the server.

## How does it works?

```
[source] --> [Client] --HOST:POST--> [Server:HOST:PORT] --> [destination]
```

## How does it runs?

- Init virtual environment
```
virtualenv -p python3 venv
```

- Activate virtual environment
```
source venv/bin/activate
```

- Install requirements.txt
```
pip install -r requirements.txt
```

- Run the Faker script and follow the instructions.
```
python faker.py --debug
```

- Run the Server script in a separate terminal and follow the instructions.
```
python server.py --debug
```

- Run the Client script in a separate terminal and follow the instructions.
```
python client.py --debug
```