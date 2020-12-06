import tkinter as tk
import tkinter.simpledialog as sdg
import tkinter.messagebox as mbx
import tkinter.font as tkf
import tkinter.filedialog as fdg
import random as rnd
import platform as pt
import time
import sys

id = "C:\\"

base = tk.Tk()
base.title("Diego G Esquivel's Visual Sorting Demo")
base.resizable(False, False)

# Fonts
fontNormal = tkf.Font(family = "Consolas", size = 10)
fontTitle = tkf.Font(family = "Consolas", size = 12, weight = "bold", slant = "italic")

frameTimes = tk.LabelFrame(base, text = "Clocked Times", bd = 4, relief = "raised", font = fontTitle)
frameTimes.grid(row = 0, column = 0, padx = 4, pady = 4, sticky = "n")

listboxTimes = tk.Listbox(frameTimes, width = 30, height = 10,  font = fontNormal)
listboxTimes.grid(row = 0, column = 0)

scrollVTimes = tk.Scrollbar(frameTimes, orient = "vertical", command = listboxTimes.yview)
scrollHTimes = tk.Scrollbar(frameTimes, orient = "horizontal", command = listboxTimes.xview)
listboxTimes.configure(yscrollcommand = scrollVTimes.set, xscrollcommand = scrollHTimes.set)
scrollVTimes.grid(row = 0, column = 1, sticky = "ns")
scrollHTimes.grid(row = 1, column = 0, columnspan = 2, sticky = "we")

def clockTime(start, end, algo):
	listboxTimes.insert("end", algo + ": " + str(round(end - start, 4)) + " sec (E=" + \
		str(elements.get()) + "; D=" + str(sleepTime.get() + sleepTimeFine.get() / 1000) + \
		" sec)" \
	)

def saveTimes():
	savefile = fdg.asksaveasfilename(parent = base, title = "Select or Enter a file to save to:", initialdir = id, filetypes = (("Text Files","*.txt"),("All Files","*.*")))

	if type(savefile) is str and len(savefile) > 0:
		file = open(savefile, "w")

		for clock in listboxTimes.get(0, "end"):
			file.write(clock + "\n")

		file.close()

buttonSaveTimes = tk.Button(frameTimes, text = "Save Times to File", bd = 2, command = saveTimes, font = fontNormal)
buttonSaveTimes.grid(row = 2, column = 0, columnspan = 2, padx = 2, pady = 2)

frameControls = tk.LabelFrame(base, text = "Sorting Controls", bd = 4, relief = "raised", font = fontTitle)
frameControls.grid(row = 0, column = 1, padx = 4, pady = 4)

frameMain = tk.LabelFrame(base, text="Sorting Panel", bd = 4, relief = "raised", font = fontTitle)
frameMain.grid(row = 1, column = 0, columnspan = 2, padx = 4, pady = 4)

frameScreen = tk.Canvas(frameMain, width = 800, height = 400)
frameScreen.pack(padx = 4, pady = 4)

elementHeights = list(range(1, 11))
elementColorCoding = {"indicated": 0, "minOrMax": -1, "sortedBorder": -1, "sortedBorderAux": -1, "sortedSide": "none"}

def processColor(element):
	colorNormal = "#2E52C4"
	colorIndicated = "#678DFF"
	colorMinOrMax = "#8D8DFF"
	colorSorted = "#002080"
	return colorMinOrMax if element == elementColorCoding["minOrMax"] else \
		colorIndicated if element == elementColorCoding["indicated"] else \
		colorSorted if element <= elementColorCoding["sortedBorder"] and \
			elementColorCoding["sortedSide"] == "left" or \
		element >= elementColorCoding["sortedBorder"] and \
			elementColorCoding["sortedSide"] == "right" or \
		( element <= elementColorCoding["sortedBorder"] or \
			element >= elementColorCoding["sortedBorderAux"]) and \
			elementColorCoding["sortedSide"] == "both" \
		else colorNormal

def clearElements():
	for el in frameScreen.find_all():
		frameScreen.delete(el)

def updateElements(strNewElements):
	try:
		newElements = int(strNewElements)
	except ValueError:
		newElements = strNewElements

	clearElements()
	global elementHeights
	max = int()
	for x in range(3, len(sys.argv) + 1,3):
		if max < int(sys.argv[x]):
			max = int(sys.argv[x])
	if newElements == 0:
		max = int()
		for x in range(3, len(sys.argv) + 1,3):
			elementHeights.append(int(sys.argv[x]))
			if max < int(sys.argv[x]):
				max = int(sys.argv[x])
		newElements = elements.get()
	else:
		for x in range(3, len(sys.argv) + 1,3):
			elementHeights.append(int(sys.argv[x]))
			if max < int(sys.argv[x]):
				max = int(sys.argv[x])
		swaps.set(0)
		comparisons.set(0)

	elWidthUnit = round(800 / newElements, 2)
	elHeightUnit = round(400 / max, 2)
	for i in range(newElements):
		frameScreen.create_rectangle(elWidthUnit * i, 400, elWidthUnit * (i + 1), 400 - elHeightUnit * elementHeights[i], fill = processColor(i), width = 0)
		frameScreen.create_text((elWidthUnit * i + elWidthUnit * (i + 1))/2, (400 - elHeightUnit * elementHeights[i]) + 10, text=elementHeights[i])

	frameScreen.update_idletasks()

elements = tk.IntVar()
elements.set(int(len(sys.argv)/3))
elementHeights = []
#print(elements.get())
############################################
#this are I can implement elements creation after arguement pass from c++ system call.#
############################################
scaleElements = tk.Scale(frameControls, label = "Sortable Elements", resolution = 1, from_ = 10, to = 800, length = 200, orient = "horizontal", variable = elements, command = updateElements, font = fontNormal, state = "disabled")
scaleElements.grid(row = 0, column = 0, rowspan = 2, padx = 2, pady = 2)
updateElements(0)


sleepTime = tk.DoubleVar()
sleepTimeFine = tk.DoubleVar()
sleepTimeSum = tk.StringVar()
sleepTimeSum.set("Time Delay: 0.0 ms")

def updateSleepTime(t):
	sleepTimeSum.set("Time Delay: " + str(sleepTime.get() * 1000 + sleepTimeFine.get()) + " ms")

scaleSleep = tk.Scale(frameControls, label = "Time Delay on Swap (Coarse)", resolution = 0.005, from_ = 0, to = 0.2, length = 200, orient = "horizontal", showvalue = False, command = updateSleepTime, variable = sleepTime, font = fontNormal)
scaleSleepFine = tk.Scale(frameControls, label = "Time Delay on Swap (Fine)", resolution = 0.1, from_ = 0, to = 4.9, length = 200, orient = "horizontal", showvalue = False, command = updateSleepTime, variable = sleepTimeFine, font = fontNormal)
labelSleep = tk.Label(frameControls, textvariable = sleepTimeSum, bd = 2, relief = "sunken", font = fontNormal)

scaleSleep.grid(row = 3, column = 0, padx = 2, pady = 2)
scaleSleepFine.grid(row = 4, column = 0, padx = 2, pady = 2)
labelSleep.grid(row = 5, column = 0, padx = 2, pady = 2)

swaps = tk.IntVar()
comparisons = tk.IntVar()

def swap(elA, elB, doDelay = True):
	if elA == elB:
		return None
	elementHeights[elA] += elementHeights[elB]
	elementHeights[elB] -= elementHeights[elA]
	elementHeights[elB] *= -1
	elementHeights[elA] -= elementHeights[elB]
	if doDelay:
		updateElements(0)
		time.sleep(sleepTime.get() + sleepTimeFine.get() / 1000)

def bubbleSort():
	elementColorCoding["sortedSide"] = "right"
	elementColorCoding["sortedBorder"] = elements.get()
	swaps.set(0)
	comparisons.set(0)
	start = time.time()

	for i in range(elements.get() - 1):
		localSwaps = 0

		for j in range(elements.get() - i - 1):
			elementColorCoding["indicated"] = j + 1
			if elementHeights[j] > elementHeights[j + 1]:
				swap(j, j + 1)
				localSwaps += 1
				lastSwap = j + 1
				swaps.set(swaps.get() + 1)

			comparisons.set(comparisons.get() + 1)

		elementColorCoding["sortedBorder"] = lastSwap

		if localSwaps == 0:
			break

	clockTime(start, time.time(), "BBL")

def insertionSort():
	elementColorCoding["sortedSide"] = "left"
	elementColorCoding["sortedBorder"] = -1
	swaps.set(0)
	comparisons.set(0)
	start = time.time()

	for i in range(1, elements.get()):
		j = i - 1
		while j >= 0 and elementHeights[j] > elementHeights[j + 1]:
			elementColorCoding["indicated"] = j
			swap(j + 1, j)
			j -= 1
			swaps.set(swaps.get() + 1)
			comparisons.set(comparisons.get() + 1)

		elementColorCoding["sortedBorder"] = i + 1

	clockTime(start, time.time(), "INS")

def minIndex(firstIndex, lastIndex):
	iMin = firstIndex
	elementColorCoding["minOrMax"] = firstIndex

	for i in range(firstIndex + 1, lastIndex):

		if elementHeights[i] < elementHeights[iMin]:
			iMin = i
			elementColorCoding["minOrMax"] = i
			updateElements(0)
			time.sleep(sleepTime.get() + sleepTimeFine.get() / 1000)

	return iMin

def selectionSort():
	elementColorCoding["sortedSide"] = "left"
	elementColorCoding["sortedBorder"] = -1
	swaps.set(0)
	comparisons.set(0)

	start = time.time()

	for i in range(1, elements.get()):
		m = minIndex(i, elements.get())
		elementColorCoding["indicated"] = -1
		elementColorCoding["minOrMax"] = m

		while m >= i and elementHeights[m] < elementHeights[m - 1]:
			elementColorCoding["minOrMax"] = m - 1
			swap(m, m - 1)
			m -= 1
			lastSwap = m
			swaps.set(swaps.get() + 1)
			comparisons.set(comparisons.get() + 1)

		elementColorCoding["sortedBorder"] = m

	clockTime(start, time.time(), "SLC")

def merge(baseLeft, lengthLeft, baseRight, lengthRight):
	localArray = elementHeights[baseLeft : baseLeft + lengthLeft + lengthRight]
	localLeft = 0
	localRight = lengthLeft

	for k in range(baseLeft, baseLeft + lengthLeft + lengthRight):
		elementColorCoding["indicated"] = k

		if localRight == lengthLeft + lengthRight or (localLeft < lengthLeft and localArray[localLeft] < localArray[localRight]):
			elementHeights[k] = localArray[localLeft]
			localLeft += 1
		else:
			elementHeights[k] = localArray[localRight]
			localRight += 1

		elementColorCoding["sortedBorder"] = k

		updateElements(0)
		time.sleep(sleepTime.get() + sleepTimeFine.get() / 1000)

def mergeInPlace(baseLeft, lengthLeft, baseRight, lengthRight):
	for i in range(baseRight + lengthRight - 1, baseRight - 1, -1):
		elementColorCoding["indicated"] = i
		j = baseLeft + lengthLeft - 1

		while j > baseLeft and elementHeights[j - 1] > elementHeights[i]:
			swap(j, j - 1, doDelay = True)
			j -= 1

		if elementHeights[j] > elementHeights[i]:
			swap(j, i)

	elementColorCoding["sortedBorder"] = baseRight + lengthRight - 1

def mergeSort(base, length, mergeFunc = merge):
	elementColorCoding["sortedSide"] = "left"
	elementColorCoding["sortedBorder"] = -1

	if length == elements.get():
		start = time.time()

	if length > 1:
		lengthLeft = length // 2
		lengthRight = length - lengthLeft
		baseLeft = base
		baseRight = base + lengthLeft

		mergeSort(baseLeft, lengthLeft, mergeFunc)
		mergeSort(baseRight, lengthRight, mergeFunc)

		mergeFunc(baseLeft, lengthLeft, baseRight, lengthRight)
		if length == elements.get():
			clockTime(start, time.time(), "MGON" if mergeFunc == merge else "MGIP")

def quickSort(left, right):
	elementColorCoding["sortedSide"] = "left"
	elementColorCoding["sortedBorder"] = left - 1

	if left == 0 and right == elements.get() - 1:
		start = time.time()

	if left < right:
		pivot = qsPartition(left, right)
		quickSort(left, pivot - 1)
		quickSort(pivot + 1, right)

	if left == 0 and right == elements.get() - 1:
		clockTime(start, time.time(), "QCK")

frameSort = tk.LabelFrame(frameControls, text = "Sorting Algorithms", bd = 2, font = fontTitle)
buttonBubble = tk.Button(frameSort, text = "Bubble", bd = 2, width = 16, command = bubbleSort, font = fontNormal)
buttonInsertion = tk.Button(frameSort, text = "Insertion", bd = 2, width = 16, command = insertionSort, font = fontNormal)
buttonSelection = tk.Button(frameSort, text = "Selection", bd = 2, width = 16, command = selectionSort, font = fontNormal)
buttonMerge = tk.Button(frameSort, text = "Merge: O(N) Space", bd = 2, width = 16, command = lambda: mergeSort(0, elements.get()), font = fontNormal)


frameSort.grid(row = 0, column = 1, rowspan = 4, padx = 2, pady = 2)

buttonBubble.grid(row = 1, column = 1, padx = 2, pady = 2)

buttonInsertion.grid(row = 1, column = 2, padx = 2, pady = 2)
buttonSelection.grid(row = 2, column = 1, padx = 2, pady = 2)

buttonMerge.grid(row = 2, column = 2, padx = 2, pady = 2)
updateElements(elements.get())
base.mainloop()