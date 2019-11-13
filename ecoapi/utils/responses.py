def isNotStation(estacion):
    """Response when station number is not found"""
    return {
        'Error': True,
        'Description': f'No station number {estacion}'
    }