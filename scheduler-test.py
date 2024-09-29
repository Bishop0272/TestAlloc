from uploadertest import write_df
from ctallocationtest import ct_alloc
from prefect import flow,task


@task
def uploader_pipeline_test():
    write_df()
    ct_alloc()


@flow(log_prints=True)
def push_to_sheet_test():
    print("Pipeline is running")
    uploader_pipeline_test()


if __name__ == "__main__":
    push_to_sheet_test()