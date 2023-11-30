
import kue from "kue";
const queue = kue.createQueue();

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw Error("Jobs is not an array");
  for (const job of jobs) {
    const jobData = {
      phoneNumber: job.phoneNumber,
      message: job.message,
    };
    const jobQueue = queue
      .create("push_notification_code_3", jobData)
      .save((err) => {
        if (!err) console.log(`Notification job created: ${jobQueue.id}`);
      });
    jobQueue.on("complete", () =>
      console.log(`Notification job ${jobQueue.id} completed`)
    );
    jobQueue.on("failed", () =>
      console.log(`Notification job ${jobQueue.id} failed`)
    );
    jobQueue.on("progress", (progress) =>
      console.log(`Notification job ${jobQueue.id} ${progress}% complete`)
    );
  }
};

export default createPushNotificationsJobs;
