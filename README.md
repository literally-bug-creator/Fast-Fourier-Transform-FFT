# Fast Fourier Transform | FFT

## What is FFT?
A ***fast Fourier transform (FFT)*** is an algorithm that computes the ***discrete Fourier transform (DFT)*** of a sequence, or its inverse (IDFT).
The ***DFT*** is obtained by decomposing a sequence of values into components of different frequencies.

## What is the difference between FFT and DFT?
This operation is useful in many fields, but computing it directly from the definition is often too slow to be practical. An FFT rapidly computes such transformations by factorizing the DFT matrix into a product of sparse (mostly zero) factors.[2] As a result, it manages to reduce the complexity of computing the DFT from $O(n^{2})$ which arises if one simply applies the definition of DFT, to $O(n\log n)$, where $n$ is the data size.
The difference in speed **can be enormous**, especially for long data sets where $n$ may be in the thousands or millions.
In the presence of round-off error, many FFT algorithms are much more accurate than evaluating the DFT definition directly or indirectly.
There are many different FFT algorithms based on a wide range of published theories, from simple complex-number arithmetic to group theory and number theory.


## Where is this operation most commonly used?
**Fast Fourier** transforms are widely used for applications in engineering, music, science, and mathematics.
The basic ideas were popularized in 1965, but some algorithms had been derived as early as 1805.
In 1994, Gilbert Strang described the FFT as "***the most important numerical algorithm of our lifetime***", and it was included in Top 10 Algorithms of 20th Century by the IEEE magazine Computing in Science & Engineering.
