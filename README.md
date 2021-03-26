# gtf2bed

This is a simple Python CLI tool to extract features from a GTF file and write them to a BED file.

Keep in mind this is a simple prototype, use it at your own risk.

## Quickstart

- [Download the example data](https://github.com/jvfe/gtf2bed/raw/main/data/Marmota_example.gtf.gz), a subset of
  the [Ensembl](https://www.ensembl.org/) Marmota marmota GTF file.

- Download package

```bash
pip install gtf2bed
```

- Run the package on the example data

```bash
gtf2bed --gtf Marmota_example.gtf.gz --output Marmota_result --feature three_prime_utr,exon
```

This will create two feature bed files, `Marmota_result_exon.bed.gz` and `Marmota_result_three_prime_utr.bed.gz`
for the corresponding features.

The command will require more RAM depending on the size of the input GTF file.

* Basic features that can be extracted:
  * `exon`
  * `intron`
  * `start_codon`
  * `stop_codon`
  * `CDS`
  * `three_prime_utr`
  * `five_prime_utr`
  * `ncRNA`
