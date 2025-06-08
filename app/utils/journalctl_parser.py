import subprocess
import time

def stream_journalctl(args=None):
    cmd = ['journalctl', '-f', '-n', '100', '--no-pager']
    if args:
        cmd.extend(args)
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            text=True,
            bufsize=1
        )
    except Exception as e:
        raise RuntimeError(f"Error running journalctl: {e}")

    def generator():
        try:
            last_activity = time.time()
            while True:
                line = process.stdout.readline()
                if line:
                    yield line
                    last_activity = time.time()
                else:
                    # If no new data for 10 seconds, close the connection
                    if time.time() - last_activity > 10:
                        break
                    time.sleep(0.1)
        except GeneratorExit:
            process.terminate()
            process.wait()
            raise
        except Exception as e:
            process.terminate()
            process.wait()
            raise RuntimeError(f"Error reading journalctl output: {e}")
        finally:
            process.terminate()
            process.wait()

    return generator()
