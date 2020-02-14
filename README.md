# Project Title

Custom IFTTT Applets

## Getting Started

```shell
python manage.py
```

### Prerequisites

1. [set up a new ifttt count](https://ifttt.com/join)
2. [create a new IFTTT applet](https://ifttt.com/create)
   1. Click on the big “this” button
   2. Search for the “webhooks” service and select the “Receive a web request” trigger
   3. Let’s name the event test_event(EVENT_NAME)
   4. Now select the big “that” button
   5. Search for the “telegram” service and select the “Send message”
   6. Change the message! and click on “Create action”
   7. Click on the “Finish” button and we’re done
3. install packages

   ```shell
   pip install -r requirements.txt
   ```

## Contributing

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
