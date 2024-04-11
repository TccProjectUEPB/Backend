from .tasks.default_admin_task import DefaultAdminTask

class BackgroundTaskService:
    def __init__(self):
        self.tasks = [DefaultAdminTask]
        #self.logger = logger

    async def start(self):
        try:
            for task in self.tasks:
                #self.logger.info("task successfuly initialized.")
                await task.run()
        except Exception as err:
            print(err)
            #self.logger.debug(f"unexpectedly stopped err: {err=}.")
            #self.logger.info("task unexpectedly stopped.")

    def stop(self):
        self.running = False