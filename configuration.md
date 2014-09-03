This is an example configuration file. The configuration specification is as follows:

- launchers
   - say hello
      - command: echo "hello" | festival --tts
      - icon: sayHello.png
   - say world
      - command: echo "world" | festival --tts
      - icon: sayWorld.png
   - wait
      - command: for ((x = 0; x < 10; ++x)); do :; done
      - icon: wait.png

This is the conclusion of this configuration specification.
