import Algorithms
import time
import os
import sys
import pygame as pg

dimensions = (1024, 512)

Algorithms = {
    "SelectionSort": Algorithms.SelectionSort(),
    "BubbleSort": Algorithms.BubbleSort(),
    "InsertionSort": Algorithms.InsertionSort(),
    "MergeSort": Algorithms.MergeSort(),
    "QuickSort": Algorithms.QuickSort(),
    "HeapSort": Algorithms.HeapSort(),
    "CountingSort": Algorithms.CountingSort(),
    "RadixSort": Algorithms.RadixSort(),
    "BucketSort": Algorithms.BucketSort()
}

window = pg.display.set_mode(dimensions)
window.fill(pg.Color("#a48be0"))

def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

def update(Algorithm, swap_index1=None, swap_index2=None, display=pg.display):
    window.fill(pg.Color("#a48be0"))
    pg.display.set_caption("{} Algorithm Visualiser   Time: {:.2f}      Status: Sorting...".format(Algorithm.name, time.time() - Algorithm.start_time))
    width = int(dimensions[0]/len(Algorithm.array))
    for i in range(len(Algorithm.array)):
        colour = (0, 0, 255)
        if swap_index1 == Algorithm.array[i]:
            colour = (0,255,0)
        elif swap_index2 == Algorithm.array[i]:
            colour = (255,0,0)
        pg.draw.rect(window, colour, (i*width,dimensions[1],width,-Algorithm.array[i]))
    pg.display.update()


def update_bucket(Algorithm, buckets, bucket_colours):
    window.fill(pg.Color("#a48be0"))
    pg.display.set_caption("{} Algorithm Visualiser   Time: {:.2f}      Status: Sorting...".format(Algorithm.name, time.time() - Algorithm.start_time))
    width = int(dimensions[0]/len(Algorithm.array))
    count = 0
    for b_index, bucket in enumerate(buckets):
        colour = bucket_colours[b_index]
        for e_index, element in enumerate(bucket):
            pg.draw.rect(window, colour, (count * width, dimensions[1], width, -element))
            count += 1
    pg.display.update()


def keep_open(Algorithm, display, time):
    pg.display.set_caption("{} Algorithm Visualiser   Time: {:.2f}      Status: Complete!".format(Algorithm.name, time))
    while True:
        check_events()

if __name__ == "__main__":
    pg.init()
    if len(sys.argv) < 2:
        print("Please select a sorting Algorithm.")
    elif sys.argv[1] == "list":
            print("Available Algorithms:\n\t" + "\n\t".join(Algorithms.keys()))
            sys.exit(0)
    else:
        Algorithm = Algorithms[sys.argv[1]]
        _, time_elapsed = Algorithm.run()
        keep_open(Algorithm, window, time_elapsed)
