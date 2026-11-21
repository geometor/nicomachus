:order: 28
:layout: book
:breadcrumb_title: Ch. 28: The Seven Additional Means (Notes)
:title: Chapter 28: The Seven Additional Means Completing the Ten Proportions — Notes
:canonical_id: Book II, Ch. 28
:original_id: D'Ooge pp. 281–284 · Hoche pp. 139–144
:folio: introductio_arithmetica:0297
:hero: /_static/figures/three-classical-means-semicircle.svg
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _nicomachus-notes-2-28:

=============================================================================
Chapter 28: The Seven Additional Means Completing the Ten Proportions — Notes
=============================================================================

.. folio:: introductio_arithmetica:0297
   :page: p. 281

Archival Witnesses & Apparatus
------------------------------

* **English Witness**: Martin Luther D'Ooge (trans.), *Nicomachus of Gerasa: Introduction to Arithmetic* (University of Michigan Studies, Vol. XVI, 1926), pp. 281–284 (folios ``introductio_arithmetica:0297``–``0300``).
* **Greek Witness**: Richard Hoche (ed.), *Nicomachi Geraseni Pythagorei Introductionis Arithmeticae Libri II* (Leipzig: Teubner, 1866), pp. 139–144 (folios ``hoche_1866:0158``–``0162``).
* **Ancient Parallels**: :person:`Pappus <pappus>`, *Synagoge* III.18–22 (:cite:`pappus:synagoge:iii`); :person:`Iamblichus <iamblichus>`, *In Nicomachi Arithmeticam* pp. 142, 162–168 Pistelli; :person:`Boethius <boethius>`, *De Institutione Arithmetica* II.51–53.

Robbins & D'Ooge Critical Notes on Means 8, 9 & 10
--------------------------------------------------

As :person:`Frank Egleston Robbins <robbins>` and :person:`Martin Luther D'Ooge <dooge>` establish in their critical notes (:cite:`dooge:1926`, pp. 282–284 nn.; cf. :cite:`heath:hgm:1921`, Vol. I, pp. 86–89), the manuscript tradition of Book II, Ch. 28.3–4 preserves two instructive slips in Nicomachus's preliminary summary list (corrected in Ch. 28.9–10 and in :person:`Iamblichus <iamblichus>` / :person:`Pappus <pappus>`):

1. **8th & 9th Means**: In the preliminary list at II.28.3 (Hoche p. 140), the manuscripts give :math:`4, 7, 8` and :math:`3, 5, 6` alongside compressed verbal phrasing ("middle among the differences"), whereas in the detailed exposition at II.28.9–10 (Hoche pp. 142–143) the 8th mean :math:`(c - a) : (c - b) = c : a` is illustrated properly by **6, 7, 9** (:math:`(9-6):(9-7) = 3:2 = 9:6`) and the 9th mean :math:`(c - a) : (b - a) = b : a` is satisfied by **4, 6, 7** (:math:`(7-4):(6-4) = 3:2 = 6:4`).
   All ten canonical proportions and closed forms are verified symbolically in ``geometor.nicomachus.compute_all_ten_means`` and ``verify_ten_means_identities``.
2. **10th Mean as the Fibonacci Recurrence**: The 10th mean :math:`(c - a) : (c - b) = b : a` expands to :math:`a(c - a) = b(c - b) \iff (b - a)(b + a - c) = 0`. Since :math:`a < b < c` guarantees :math:`b \neq a`, this reduces identically to **the Fibonacci additive law** :math:`a + b = c`, which is why Nicomachus's exemplar :g:`(3, 5, 8) <three-classical-means-semicircle:MEAN10>` consists of three consecutive Fibonacci numbers!
3. **Eudemus / Pappus Attribution**: :person:`Pappus <pappus>` (*Synagoge* III.18–22) attributes the discovery of means 4–6 to :person:`Eudoxus <eudoxus>` (or Pythagoreans) and means 7–10 to later Neo-Pythagoreans such as Myonides and Euphranor (:cite:`heath:hgm:1921`, Vol. I, p. 86).
