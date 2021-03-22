from click.testing import CliRunner
from gtf2bed.main import gtf2bed


def test_basic_function():

    command = "--gtf data/Marmota_example.gtf.gz --output results/Marmota_result --feature three_prime_utr"
    runner = CliRunner()
    result = runner.invoke(gtf2bed, command.split())

    assert result.exit_code == 0


def test_multiple_features():

    command = "--gtf data/Marmota_example.gtf.gz --output results/Marmota_result --feature three_prime_utr,exon"
    runner = CliRunner()
    result = runner.invoke(gtf2bed, command.split())

    assert result.exit_code == 0