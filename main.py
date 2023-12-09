import argparse
import csiread
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, help='path to csi data')
args = parser.parse_args()

tx_num = 2
rx_num = 3

csidata = csiread.Intel(args.path)
csidata.read()
csi = csidata.get_scaled_csi()

print(csidata.display(2))

fig, axs = plt.subplots(tx_num+1, 2, figsize=(14, 6))
fig.subplots_adjust(hspace=0.7, wspace=0.2)
x = np.arange(30)

for tx in range(tx_num):
    axs[tx, 0].set_title(f'tx ant{tx}')
    axs[tx, 0].set_xlabel('subcarriers')
    axs[tx, 0].set_ylabel('amplitude')
    axs[tx, 1].set_title(f'tx ant{tx}')
    axs[tx, 1].set_xlabel('subcarriers')
    axs[tx, 1].set_ylabel('phase')

amplis = [[axs[tx, 0].plot(x, csi[0, :, rx, tx].real, label=f'rx ant{rx}')[0]
           for rx in range(rx_num)]for tx in range(tx_num)]
phases = [[axs[tx, 1].plot(x, csi[0, :, rx, tx].imag, label=f'rx ant{rx}')[0]
           for rx in range(rx_num)]for tx in range(tx_num)]

axs[tx_num, 0].set_xlabel('packets')
axs[tx_num, 0].set_ylabel('amplitude')
for rx in range(rx_num):
    axs[tx_num, 0].plot(csi[:, 0, rx, 0].real, label=f'rx ant{rx}')

axs[tx_num, 1].set_xlabel('packets')
axs[tx_num, 1].set_ylabel('phase')
for rx in range(rx_num):
    axs[tx_num, 1].plot(csi[:, 0, rx, 0].imag, label=f'rx ant{rx}')


# def animate(i):
#     return None

# ani = animation.FuncAnimation(
#     fig, animate, interval=200, blit=True)

fig.legend()
plt.show()
