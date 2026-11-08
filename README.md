# Flask Stack and Queue Simulators

This repository contains two independent Flask data-structure demonstrations:

- `stack-simulator/` demonstrates **Last In, First Out (LIFO)** with Push, Pop,
  Peek, and Clear.
- The repository root demonstrates **First In, First Out (FIFO)** with Enqueue,
  Dequeue, Peek, and Clear.

## Run the queue simulator

```powershell
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

## Run the stack simulator

Open a second terminal and run:

```powershell
cd stack-simulator
python -m pip install -r ..\requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` after stopping the queue simulator, or configure a
different Flask port when running both applications at the same time.