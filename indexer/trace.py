import contextvars
from datetime import datetime
from pathvalidate import sanitize_filename
import json
import os

class Trace():
    _current_trace: contextvars.ContextVar["Trace"] = contextvars.ContextVar(
        "current_trace", default=None
    )

    def __init__(self, id):
        self.id = f"{str(datetime.now())}-{sanitize_filename(id.replace(" ", "_"))}"
        self.events = []

    @classmethod
    def start(cls, id):
        trace = cls(id)
        cls._current_trace.set(trace)
        return trace

    @classmethod
    def get(cls):
        return cls._current_trace.get()
    
    @classmethod
    def log(cls, event):
        trace = cls.get()
        trace.events.append({"timestamp": str(datetime.now()), "event": event})

    @classmethod
    def dump(cls):
        dump_folder = ".traces"
        if not os.path.exists(dump_folder):
            os.makedirs(dump_folder)    

        trace = cls.get()
        trace_string = "\n\n".join([json.dumps(e) for e in trace.events])

        with open(f"{dump_folder}/{trace.id}.jsonl", "w") as f:
            f.write(trace_string)