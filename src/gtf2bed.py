from gtfparse import read_gtf
import logging
import click

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    level=logging.INFO,
)


@click.command()
@click.option(
    "--gtf",
    required=True,
    help="The input GTF file",
    type=click.Path(readable=True, exists=True),
)
@click.option(
    "--output",
    required=True,
    help="The name of the output BED file.",
    type=click.Path(writable=True),
)
@click.option(
    "--feature",
    required=True,
    help="The name of the feature of the GTF you want to extract.",
)
@click.option(
    "--compressed",
    default=True,
    help="Whether to output a compressed BED file.",
    type=click.BOOL,
)
def gtf2bed(gtf, output, feature, compressed):
    """Simple command to convert GTF features to a BED file"""

    logging.info(f"Reading {gtf}...")
    current_gtf = read_gtf(gtf, chunksize=1024)

    features = set([feature])
    logging.info(f"Filtering {gtf} for {'; '.join(features)}...")
    feature_gtf = current_gtf[current_gtf["feature"].isin(features)]

    bed_data = feature_gtf[
        ["seqname", "start", "end", "gene_id", "score", "strand"]
    ].fillna(".")

    logging.info(f"Writing {output}...")
    if compressed:
        bed_data.to_csv(
            f"{output}.bed.gz",
            sep="\t",
            compression="gzip",
            header=False,
            index=False,
            chunksize=1024,
        )
    else:
        bed_data.to_csv(
            f"{output}.bed",
            sep="\t",
            header=False,
            index=False,
            chunksize=1024,
        )