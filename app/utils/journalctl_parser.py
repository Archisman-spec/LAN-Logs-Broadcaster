import subprocess

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
            for line in process.stdout:
                yield line
        finally:
            process.terminate()
            process.wait()

    return generator()
