Python 3 comes with a large standard library of built-in modules that provide a wide range of functionality. Here's a list of some of the most commonly used built-in modules in Python 3:

### Core Modules
1. **`__future__`** - Compatibility features.
2. **`abc`** - Abstract Base Classes.
3. **`aifc`** - Read and write AIFF and AIFC files.
4. **`argparse`** - Command-line option and argument parsing library.
5. **`array`** - Efficient arrays of numeric values.
6. **`ast`** - Abstract Syntax Trees.
7. **`asynchat`** - Asynchronous socket command/response handler.
8. **`asyncio`** - Asynchronous I/O, event loop, coroutines, tasks.
9. **`asyncore`** - Asynchronous socket handler.
10. **`atexit`** - Register functions to be called when a program is closing down.
11. **`audioop`** - Manipulate raw audio data.
12. **`base64`** - Encode and decode files using the base64 alphabet.
13. **`bdb`** - Debugger framework.
14. **`binascii`** - Convert between binary and ASCII.
15. **`binhex`** - Encode and decode binhex4 files.
16. **`bisect`** - Array bisection algorithms.
17. **`builtins`** - Built-in objects.
18. **`bz2`** - Interface for bzip2 compression.
19. **`calendar`** - General calendar-related functions.
20. **`cgi`** - Common Gateway Interface support.
21. **`cgitb`** - Traceback manager for CGI scripts.
22. **`chunk`** - Read IFF chunked data.
23. **`cmath`** - Mathematical functions for complex numbers.
24. **`cmd`** - Support for line-oriented command interpreters.
25. **`code`** - Interpreter base classes.
26. **`codecs`** - Codec registry and base classes.
27. **`codeop`** - Compile Python code.
28. **`collections`** - High-performance container datatypes.
29. **`colorsys`** - Conversion functions between color systems.
30. **`compileall`** - Tools to compile all Python source files in a directory tree.
31. **`concurrent.futures`** - Launch parallel tasks.
32. **`configparser`** - Configuration file parser.
33. **`contextlib`** - Utilities for with-statement contexts.
34. **`copy`** - Shallow and deep copy operations.
35. **`copyreg`** - Register pickle support functions.
36. **`crypt`** - Function to check Unix passwords.
37. **`csv`** - CSV file reading and writing.
38. **`ctypes`** - A foreign function library for Python.
39. **`curses`** - Terminal handling for character-cell displays.
40. **`dataclasses`** - Data classes.
41. **`datetime`** - Basic date and time types.
42. **`dbm`** - Interfaces to Unix databases.
43. **`decimal`** - Decimal fixed-point and floating-point arithmetic.
44. **`difflib`** - Helpers for computing deltas.
45. **`dis`** - Disassembler for Python bytecode.
46. **`distutils`** - Support for building and installing Python packages.
47. **`doctest`** - Test interactive Python examples.
48. **`dummy_threading`** - Drop-in replacement for the threading module.
49. **`email`** - Package for managing email messages.
50. **`encodings`** - Standard Encodings.
51. **`ensurepip`** - Bootstrapping the pip installer.
52. **`enum`** - Support for enumerations.
53. **`errno`** - Standard errno system symbols.
54. **`faulthandler`** - Dump the Python traceback.
55. **`fcntl`** - The fcntl and ioctl system calls.
56. **`filecmp`** - Compare files.
57. **`fileinput`** - Iterate over lines from multiple input streams.
58. **`fnmatch`** - Unix filename pattern matching.
59. **`fractions`** - Rational numbers.
60. **`ftplib`** - FTP protocol client.
61. **`functools`** - Higher-order functions and operations on callable objects.
62. **`gc`** - Garbage Collector interface.
63. **`getopt`** - C-style parser for command line options.
64. **`getpass`** - Portable password input.
65. **`gettext`** - Multilingual internationalization services.
66. **`glob`** - Unix style pathname pattern expansion.
67. **`grp`** - Unix group database.
68. **`gzip`** - Support for gzip files.
69. **`hashlib`** - Secure hash and message digest algorithms.
70. **`heapq`** - Heap queue algorithm.
71. **`hmac`** - Keyed-Hashing for Message Authentication.
72. **`html`** - HyperText Markup Language support.
73. **`http`** - HTTP modules.
74. **`idlelib`** - Python IDE built with tkinter.
75. **`imaplib`** - IMAP4 protocol client.
76. **`imghdr`** - Determine the type of an image.
77. **`imp`** - Access the implementation of the import statement.
78. **`importlib`** - The implementation of the import statement.
79. **`inspect`** - Inspect live objects.
80. **`io`** - Core tools for working with streams.
81. **`ipaddress`** - IPv4/IPv6 manipulation library.
82. **`itertools`** - Functions creating iterators for efficient looping.
83. **`json`** - JSON encoder and decoder.
84. **`keyword`** - Test whether a string is a keyword.
85. **`lib2to3`** - The 2to3 library.
86. **`linecache`** - Random access to text lines.
87. **`locale`** - Internationalization services.
88. **`logging`** - Flexible event logging system.
89. **`lzma`** - Compression using the LZMA algorithm.
90. **`mailbox`** - Manipulate mailboxes in various formats.
91. **`mailcap`** - Mailcap file handling.
92. **`marshal`** - Internal Python object serialization.
93. **`math`** - Mathematical functions.
94. **`mimetypes`** - Map filenames to MIME types.
95. **`mmap`** - Memory-mapped file support.
96. **`modulefinder`** - Find modules used by a script.
97. **`msvcrt`** - Useful routines from the MS VC++ runtime.
98. **`multiprocessing`** - Process-based parallelism.
99. **`netrc`** - netrc file processing.
100. **`nis`** - Interface to Sun's NIS (Yellow Pages).
101. **`nntplib`** - NNTP protocol client.
102. **`numbers`** - Numeric abstract base classes.
103. **`operator`** - Standard operators as functions.
104. **`optparse`** - Command-line option parsing library.
105. **`os`** - Miscellaneous operating system interfaces.
106. **`ossaudiodev`** - Access to OSS-compatible audio devices.
107. **`parser`** - Access Python parse trees.
108. **`pathlib`** - Object-oriented filesystem paths.
109. **`pdb`** - The Python debugger.
110. **`pickle`** - Python object serialization.
111. **`pickletools`** - Tools for pickle developers.
112. **`pipes`** - Interface to shell pipelines.
113. **`pkgutil`** - Utilities for the import system.
114. **`platform`** - Access to underlying platform’s identifying data.
115. **`plistlib`** - Generate and parse Mac OS X .plist files.
116. **`poplib`** - POP3 protocol client.
117. **`posix`** - The most common POSIX system calls.
118. **`pprint`** - Data pretty printer.
119. **`profile`** - Python source profiler.
120. **`pstats`** - Statistics object for use with the profiler.
121. **`pty`** - Pseudo-terminal utilities.
122. **`pwd`** - The password database.
123. **`py_compile`** - Compile Python source files.
124. **`pyclbr`** - Python class browser support.
125. **`pydoc`** - Documentation generator and online help system.
126. **`queue`** - A synchronized queue class.
127. **`quopri`** - Encode and decode MIME quoted-printable data.
128. **`random`** - Generate pseudo-random numbers.
129. **`re`** - Regular expression operations.
130. **`readline`** - GNU readline interface.
131. **`reprlib`** - Alternate repr() implementation.
132. **`resource`** - Resource usage information.
133. **`rlcompleter`** - GNU readline completion.
134. **`runpy`** - Locate and run Python programs using the module name.
135. **`sched`** - Event

 scheduler.
136. **`secrets`** - Generate secure random numbers for managing secrets.
137. **`select`** - Wait for I/O completion.
138. **`selectors`** - High-level I/O multiplexing.
139. **`shelve`** - Python object persistence.
140. **`shlex`** - Simple lexical analysis.
141. **`shutil`** - High-level file operations.
142. **`signal`** - Set handlers for asynchronous events.
143. **`site`** - Site-specific configuration hook.
144. **`smtpd`** - SMTP server implementation.
145. **`smtplib`** - SMTP protocol client.
146. **`sndhdr`** - Determine type of sound file.
147. **`socket`** - Low-level networking interface.
148. **`socketserver`** - A framework for network servers.
149. **`sqlite3`** - DB-API 2.0 interface for SQLite databases.
150. **`ssl`** - TLS/SSL wrapper for socket objects.
151. **`stat`** - Interpret stat() results.
152. **`statistics`** - Mathematical statistics functions.
153. **`string`** - Common string operations.
154. **`stringprep`** - String preparation.
155. **`struct`** - Interpret bytes as packed binary data.
156. **`subprocess`** - Subprocess management.
157. **`sunau`** - Read and write Sun AU files.
158. **`symbol`** - Constants used with Python parse trees.
159. **`symtable`** - Access to the compiler’s symbol tables.
160. **`sys`** - System-specific parameters and functions.
161. **`sysconfig`** - Python's configuration information.
162. **`tabnanny`** - Detection of ambiguous indentation.
163. **`tarfile`** - Read and write tar archive files.
164. **`telnetlib`** - Telnet client.
165. **`tempfile`** - Generate temporary files and directories.
166. **`termios`** - POSIX style tty control.
167. **`textwrap`** - Text wrapping and filling.
168. **`this`** - The Zen of Python.
169. **`threading`** - Thread-based parallelism.
170. **`time`** - Time access and conversions.
171. **`timeit`** - Measure execution time of small code snippets.
172. **`tkinter`** - Python interface to Tcl/Tk.
173. **`token`** - Constants used with Python parse trees.
174. **`tokenize`** - Tokenizer for Python source.
175. **`trace`** - Trace or track Python statement execution.
176. **`traceback`** - Print or retrieve a stack traceback.
177. **`tracemalloc`** - Trace memory allocations.
178. **`tty`** - Terminal control functions.
179. **`turtle`** - Turtle graphics.
180. **`turtledemo`** - Turtle graphics examples.
181. **`types`** - Dynamic type creation and names for built-in types.
182. **`typing`** - Support for type hints.
183. **`unicodedata`** - Unicode database.
184. **`unittest`** - Unit testing framework.
185. **`urllib`** - URL handling modules.
186. **`uu`** - Encode and decode uuencoded files.
187. **`uuid`** - UUID objects according to RFC 4122.
188. **`venv`** - Creation of virtual environments.
189. **`warnings`** - Warning control.
190. **`wave`** - Read and write WAV files.
191. **`weakref`** - Weak references.
192. **`webbrowser`** - Convenient web-browser controller.
193. **`winreg`** - Windows registry access.
194. **`winsound`** - Sound-playing interface for Windows.
195. **`wsgiref`** - WSGI Utilities and Reference Implementation.
196. **`xdrlib`** - Encode and decode XDR data.
197. **`xml`** - XML processing modules.
198. **`xmlrpc`** - XML-RPC server and client modules.
199. **`zipapp`** - Manage executable Python zip archives.
200. **`zipfile`** - Read and write ZIP files.
201. **`zipimport`** - Import modules from ZIP archives.
202. **`zlib`** - Compression compatible with gzip.

These modules cover a wide range of tasks from file I/O, text processing, data serialization, concurrency, networking, to database access, and much more. For a complete list and detailed documentation, refer to the [official Python documentation](https://docs.python.org/3/library/index.html).