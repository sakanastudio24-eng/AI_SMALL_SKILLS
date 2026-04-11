type Job = {
  id: string;
  orderId: string;
};

export async function processJob(job: Job) {
  const alreadyProcessed = await hasProcessed(job.id);
  if (alreadyProcessed) {
    return { status: "duplicate_ignored" };
  }

  await markProcessing(job.id);
  await generateInvoice(job.orderId);
  await markProcessed(job.id);

  return { status: "ok" };
}

async function hasProcessed(_jobId: string) {
  return false;
}

async function markProcessing(_jobId: string) {
  return;
}

async function generateInvoice(_orderId: string) {
  return;
}

async function markProcessed(_jobId: string) {
  return;
}
