from gtfparse import read_gtf
from .constants import FEATURES, NON_CODING_BIOTYPES
import logging
import click

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
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
    help="A comma-separated list of feature names to extract.",
    type=click.STRING,
)
@click.option(
    "--compressed",
    default=True,
    help="Whether to output a compressed BED file.",
    type=click.BOOL,
)
def gtf2bed(gtf, output, feature, compressed):
    """Simple command to convert GTF features to a BED file"""

    # TODO: Support the following features:
    ## On feature column (Done):
    # 5’ UTR
    # 3’ UTR
    # CDS
    # Exons
    # Introns
    # Start codons
    # Stop codons
    ## Computed:
    # Non-coding RNA (Done)
    # First exons
    # Last Exons

    feature_list = set(feature.split(","))

    logging.info(f"Reading {gtf}...")
    current_gtf = read_gtf(gtf, chunksize=1024)

    logging.info(f"Filtering {gtf} for {'; '.join(feature_list)}...")
    feature_gtf = current_gtf[current_gtf["feature"].isin(feature_list)]

    if "ncRNA" in feature_list:
        feature_gtf = feature_gtf[
            feature_gtf["transcript_biotype"].isin(NON_CODING_BIOTYPES)
        ]

    if feature_gtf.empty:
        nl = "\n"
        message = f"File is empty, check that the feature provided is contained below:\n{nl.join(FEATURES)}"
        logging.error(message)
        raise Exception

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