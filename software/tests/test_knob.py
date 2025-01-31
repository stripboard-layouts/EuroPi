import pytest

from europi import k1, k2, MAX_UINT16

from mock_hardware import MockHardware


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 1.0000),
        (MAX_UINT16 / 4, 0.7500),
        (MAX_UINT16 / 3, 0.6667),
        (MAX_UINT16 / 2, 0.5000),
        (MAX_UINT16, 0.0000),
    ],
)
def test_percent(mockHardware: MockHardware, value, expected):
    mockHardware.set_ADC_u16_value(k1, value)

    assert round(k1.percent(), 4) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 99),
        (MAX_UINT16 / 4, 74),
        (MAX_UINT16 / 3, 66),
        (MAX_UINT16 / 2, 49),
        (MAX_UINT16, 0),
    ],
)
def test_read_position(mockHardware: MockHardware, value, expected):
    mockHardware.set_ADC_u16_value(k1, value)

    assert k1.read_position() == expected


def test_knobs_are_independent(mockHardware: MockHardware):
    mockHardware.set_ADC_u16_value(k1, 0)
    mockHardware.set_ADC_u16_value(k2, MAX_UINT16)

    assert k1.percent() == 1.0
    assert k2.percent() == 0.0
