# chill is more preferable
import math
import plotly.graph_objects as go


E = 5  # number of digits (precision)


def cooling_gen(
        ts: [int, float], t0: [int, float], r: [int, float],
        dt: [int, float], t=0
):
    """
    Return result of the Newton's law of cooling function in differential form
    :param ts: Start temperature of environment Celsius
    :param t0: Start temperature of liquid Celsius
    :param r: Cooling coefficient
    :param dt: Differential of time function
    :param t: Start time
    :return:
    """

    while True:
        yield t, round(ts + (t0 - ts) * math.exp(-r*t), E)
        t = round(t + dt, E)


if __name__ == '__main__':
    TS = 22
    T0 = 83
    R = 0.0373
    dT = 0.1

    COMFORTABLE_TEMPERATURE = 30  # Celsius

    # coordinates
    x = []
    y = []

    gen = cooling_gen(TS, T0, R, dT)
    while True:
        time, temp = next(gen)

        x.append(time)
        y.append(temp)

        print(f'Время, с {time}; Температура °C {temp}')

        if temp <= COMFORTABLE_TEMPERATURE:
            break

    if x and y:
        fig = go.Figure(data=go.Scatter(x=x, y=y))
        fig.show()
