# Unified Forth (u4th)

## NOT WORKING YET

The aim of this Forth is running [Standard](https://forth-standard.org/) Forth code inside all programming languages' projects.

Aim in points:
- [ ] Pass all [Standard Forth tests](https://forth-standard.org/standard/testsuite)
- [ ] Each implementation execute functions of the parent language
- [ ] All of Standard Forth be written in Forth itself except the absolute necessary words of [core](https://forth-standard.org/standard/core)
- [ ] Each language have a folder with two folders inside.
    * normal: where the code is easiest to read
    * fast  : where the code is fastest
- [ ] Contain a two step tree-shaking capability
    * run your code with a certain flag. the program prints the unused words (your words and system words)
    * send these words using another flag to produce a dictionary that excludes the unused words.


## Implementation details
* The dictionary is an array of bytes (not sure yet)
* Each internal word is a procedure/function in the parent language. And each has a numerical index.
* If the interpreter sees the index of an internal function, it will call it.


## License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** License.

You are free to use, modify, and distribute the code, including for commercial purposes, as long as you give appropriate credit to this repository. Please include a clear attribution in your project where users can easily find it.

For full details, see the [LICENSE](./LICENSE.md).
