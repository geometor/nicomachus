:order: 1
:layout: book
:breadcrumb_title: Philosophy & Primes (Notes)
:title: Philosophy, the Quadrivium, the Odd Sieve & Perfect Numbers — Notes
:canonical_id: Book I, Chs. 1–7, 13, 16
:original_id: Hoche pp. 1–14, 29–36, 39–44
:folio: Book I, Chs. 1–7, 13, 16
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _unit-1-philosophy-quadrivium-primes-notes:
.. _sec_01_philosophy_quadrivium_primes-notes:

===============================================================================================
Unit I — Philosophy, the Quadrivium, the Odd Sieve & Perfect Numbers — Critical Commentary
===============================================================================================

.. rubric:: Greek Philology, Exact Number-Theoretic Analysis & Boethian Quadrivium Reception · Book I, Chs. 1–7, 13, 16

.. picture:: /_static/figures/sieve-perfect-numbers.svg
   :alt: Nicomachus's Odd Sieve of Eratosthenes and Perfect Numbers
   :caption: Exact odd-sequence Sieve of Eratosthenes (I.13) and Mersenne prime generation of Perfect Numbers 6, 28, 496, 8128 (I.16).

I. From Nicomachus's *Tessares Methodoi* to Boethius's *Quadrivium* (I.1–6)
---------------------------------------------------------------------------

1. **Poson vs. Pēlikon and Aristotle's Categories**:
   In :cite:`aristotle:cat:4b20` (*Categories* 6, 4b20), :person:`Aristotle <aristotle>` divided quantity (*to poson*) into discrete (number and speech) and continuous (line, surface, body, time, place). Nicomachus refines the terminology by reserving :term:`poson <poson>` (*multitudo*) strictly for bounded discrete multitude and :term:`pelikon <pelikon>` (*magnitudo*) for bounded continuous magnitude. Five centuries later, :person:`Proclus <proclus>` reproduces Nicomachus's fourfold schema verbatim in his Prologue to :person:`Euclid <euclid>` (:cite:`proclus:in-euclid:35-37`, pp. 35.17–36.25 Friedlein), while :person:`Boethius <boethius>` renders Nicomachus's "four methods" (*tessares methodoi*), "bridges" (*gephyrai*), and "ladders" (*klimakes*) by the newly minted Latin compound **quadruvium** ("fourfold crossroads") at *De Institutione Arithmetica* I.1 (:cite:`boethius:friedlein:1867`, p. 7.25).
2. **Asymmetric Co-Removal (*Synanairein*, I.4–5)**:
   Nicomachus's proof that :g:`Arithmetic precedes Geometry, Music, and Astronomy <quadrivium-tetrad:PRIORITY>` adapts the Academic and Peripatetic test of ontological priority: :math:`A` is prior by nature to :math:`B` when abolishing :math:`A` abolishes :math:`B` (*synanairei*), whereas abolishing :math:`B` leaves :math:`A` intact (*ou synanaireitai*). Every polygon, polyhedron, and musical ratio presupposes pure cardinal integerhood (*triangle* presupposes :math:`3`; *hemiolios* presupposes :math:`3` and :math:`2`), whereas integers require neither spatial extension nor audible strings. In the thirteenth century, :person:`Thomas Aquinas <aquinas>` analyzes this exact Boethian-Nicomachean hierarchy in *Super Boethium De Trinitate* q. 5 (:cite:`aquinas:in-boethium-trinitate`).
3. **Number in the Mind of the Creator (I.6.1)**:
   By relocating Plato's Forms into the *dianoia* of the World-Creating God (*en tēi tou kosmopoiou theou dianoiāi*) as a cosmic preliminary sketch (*prokentēma*) and archetype (*archetypon paradeigma*), Nicomachus forged the exemplarism linking Middle Platonism to Christian, Islamic, and Renaissance mathematical cosmology down to :person:`Luca Pacioli <pacioli>` (:cite:`pacioli:divina-proportione:1509`) and :person:`Johannes Kepler <kepler>`.

II. Why Nicomachus's Sieve Operates Strictly on Odd Numbers (I.13)
------------------------------------------------------------------

In ``geometor.nicomachus.sieve_of_eratosthenes``, we preserve a crucial historical feature of Greek arithmetic often obscured in modern textbooks:

* For Nicomachus, neither the :term:`monad <monas>` (:math:`1`, the "seed" rather than an actual multitude) nor the dyad (**2**, the principle of the *even* genus, D'Ooge p. 204 n. 1) belongs to the genus of :term:`prime and incomposite <protos-asynthetos>` numbers, which Nicomachus defines strictly as a **subspecies of the odd**!
* Consequently, :person:`Eratosthenes's <eratosthenes>` :term:`Sieve <koskinon>` sets out **only the odd numbers** :math:`a_m = 2m + 3` (:math:`m = 0, 1, 2, \dots`). When sieving with an odd prime :math:`p` (:g:`3 <sieve-perfect-numbers:P3>`, :g:`5 <sieve-perfect-numbers:P5>`, :g:`7 <sieve-perfect-numbers:P7>`), one passes over :math:`p - 1` odd entries—advancing by **stride** :math:`p` in the odd array, which equals :math:`2p` in natural integers (:g:`3 -> 9 -> 15 -> 21 <sieve-perfect-numbers:SIEVE3>`, :g:`5 -> 15 -> 25 -> 35 <sieve-perfect-numbers:SIEVE5>`)—automatically skipping all even multiples :math:`2p, 4p, 6p`.
* Furthermore, Nicomachus misstates (or leaves ambiguous in I.11–13) one subtlety caught by :person:`Euclid <euclid>`: two odd numbers can **both** be secondary/composite in themselves and yet **not** be coprime (e.g., :g:`15 <sieve-perfect-numbers:P15>` and :math:`21` share common measure :math:`3`), which is why Nicomachus illustrates his third class specifically with :math:`9 = 3^2` and :math:`25 = 5^2` and confirms coprimality via Euclidean *anthyphairesis* (reciprocal subtraction, I.13.11–13; cf. *Elements* VII.1–2).

III. Perfect Numbers & Nicomachus's Two Famous Conjectures (I.16)
-----------------------------------------------------------------

In ``geometor.nicomachus.euclid_nicomachus_perfect_numbers``, :g:`Euclid's theorem (Elements IX.36) <sieve-perfect-numbers:MERSENNE>` generates even perfect numbers whenever :math:`M_p = 2^p - 1` is prime:

.. math::

   P_p = 2^{p-1}(2^p - 1) \quad \text{for } p \in \{2, 3, 5, 7\} \implies P_p \in \{6,\; 28,\; 496,\; 8128\}.

In I.16.3, however, Nicomachus extrapolates from these first four values two celebrated empirical generalizations (transmitted unchallenged through :person:`Boethius <boethius>` and medieval Europe for over a millennium; see :cite:`heath:hgm:1921`, Vol. I, p. 100 and :cite:`dooge:1926`, p. 210 n. 2):

1. **One perfect number per decimal order of magnitude** (units, tens, hundreds, thousands, ...): **False** from the fifth perfect number onward! Since :math:`M_{11} = 2^{11} - 1 = 2047 = 23 \times 89` is composite, there is **no** five-digit, six-digit, or seven-digit perfect number; the fifth perfect number (:math:`p = 13`) leaps to eight digits: :math:`2^{12}(2^{13} - 1) = 33{,}550{,}336`.
2. **Strict alternation of terminal digits** ``6, 8, 6, 8, ...``: **Partially true, partially false!** Every even perfect number **does** end in either ``6`` or ``8`` (provable mod :math:`10` from :math:`p \equiv 1` vs. :math:`3 \pmod{4}` for odd primes :math:`p`), **but they do not alternate strictly**: the fifth (:math:`p = 13`, :math:`33{,}550{,}336`) and sixth (:math:`p = 17`, :math:`8{,}589{,}869{,}056`) **both** end in ``6``!
