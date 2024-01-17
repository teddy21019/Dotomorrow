# Dotomorrow

Dotomorrow is a Python package designed to facilitate the interruption and resumption of for loops involving time-consuming evaluations. With Dotomorrow, users can interrupt the execution of a loop and seamlessly resume the process during the next run, saving time and resources.

## Installation

You can install Dotomorrow using pip:

```bash
pip install -i https://test.pypi.org/simple/ dotomorrow
```

## Getting Started

### Basic Usage

Here's a simple example of a time-consuming for loop:

```python
from time import sleep

# Code that has to rerun when interrupted:
results = []
for par in range(2000):
    result = 1 + par
    sleep(1)
    results.append(result)
```
When this process is interrupted, whether manually or due to an error, the prior progress is lost.

Manually saving progress involves writing a saving function at the end of the for loop, filtering the elements previously executed before the for loop for the next iteration.

Dotomorrow simplifies this process by introducing a convenient `with ... as` syntax:

```python
from dotomorrow import SavedIterator

# save and load results from the `cache.pk` file
with SavedIterator("cache.pk", [1, 2, 3, 4, 5]) as si:
    for par in si:
        result = 1 + par
        sleep(1)

        # add result to the SavedIterator object
        si += result

# Retrieve results as dict
print(si.results)   # {1: 2, 2: 3, 3: 4,...}
```

In this example, the loop's progress is saved using Dotomorrow's `SavedIterator`. If the loop is interrupted, the iterator can resume execution from where it left off in the next run.

### Features

- **Interrupt and Resume**: Dotomorrow allows users to interrupt for loops involving time-consuming evaluations and resume the process seamlessly during the next run.

- **Result Storage**: The package conveniently stores results obtained during interrupted loops, ensuring that no progress is lost.

- **Easy Integration**: Dotomorrow can be easily integrated into existing code with minimal changes, enhancing the efficiency of processes involving lengthy computations.

- **Compatibility**: Dotomorrow is compatible with other wrapping functions such as `tqdm` or `enumerate`. For example:
```python
from tqdm import tqdm

with SavedIterator("cache.pk", [1, 2, 3, 4, 5]) as si:
    for i, par in tqdm(enumerate(si)):
        result = 1 + i * par
        sleep(1)

        # add result to the SavedIterator object
        si += result
```

## Contributing

We welcome contributions from the community. If you encounter any issues, have suggestions for improvements, or want to contribute new features, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/teddy21019/dotomorrow).

For a walkthrough of the technical details behind this project, checkout my [medium article](https://ted21019.medium.com/code-behind-dotomorrow-context-manager-in-python-194c3d20d748)

## License

This project is licensed under the MIT License.

## Acknowledgments

- Dotomorrow is inspired by the need to efficiently handle interruptions in time-consuming computations.
- Special thanks to the Python community for providing valuable tools and libraries, and chatGPT for generating this README.

## Contact

For any questions or inquiries, please contact [teddychenster@gmail.com].

Happy coding with Dotomorrow!
