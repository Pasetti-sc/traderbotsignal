from iqoptionapi.stable_api import IQ_Option


def connect_iq(email: str, password: str):
    iq = IQ_Option(email, password)
    try:
        iq.connect()
        if iq.check_connect():
            return iq
    except Exception:
        pass
    return None
