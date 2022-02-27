![image](https://user-images.githubusercontent.com/100521999/155894304-edb6a524-e160-4de5-911b-b5556a9d3f29.png)
![image](https://user-images.githubusercontent.com/100521999/155894325-37f80952-b8c5-4e4f-b4ca-b01c32fb37e9.png)
![image](https://user-images.githubusercontent.com/100521999/155894336-103532e9-2490-4c23-b22a-c81109c43cfc.png)
![image](https://user-images.githubusercontent.com/100521999/155894349-a90106e9-c65c-48cf-a423-93f1bf3b93b5.png)
![image](https://user-images.githubusercontent.com/100521999/155894361-3ee8b66a-1f7c-4b79-8288-0a341c2c4096.png)
![image](https://user-images.githubusercontent.com/100521999/155894374-ec5761c9-7aca-462f-a8c7-5dd7b2e333e2.png)

Implementation

The implementation of the above algorithm heavily depends on the programming language that one chooses, since different languages provide different constructs for the concurrency mechanism. Though some of the constructs such as mutex and semaphore are present across several programming languages including Java, C++ and Python.

Here we provide a few examples using different constructs across the languages. In particular, one could find a nice summary in the Discussion forum about the concurrency constructs in Python.
```
from threading import Lock

class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        with self.firstJobDone:
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # Wait for the second job to be done.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()
