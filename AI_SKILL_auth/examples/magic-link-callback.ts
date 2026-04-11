import type { Request, Response } from "express";

export async function handleMagicLinkCallback(req: Request, res: Response) {
  const token = req.query.token;
  const next = typeof req.query.next === "string" ? req.query.next : "/app";

  if (typeof token !== "string" || token.length === 0) {
    return res.status(400).json({ error: "missing_token" });
  }

  const record = await findMagicLinkToken(token);
  if (!record || record.usedAt || record.expiresAt.getTime() < Date.now()) {
    return res.status(401).json({ error: "invalid_or_expired_token" });
  }

  await markMagicLinkUsed(record.id);

  req.session.userId = record.userId;
  req.session.authMethod = "magic_link";

  return res.redirect(safeRedirect(next));
}

async function findMagicLinkToken(token: string) {
  return {
    id: "tok_123",
    userId: "user_123",
    usedAt: null as Date | null,
    expiresAt: new Date(Date.now() + 60_000),
  };
}

async function markMagicLinkUsed(_tokenId: string) {
  return;
}

function safeRedirect(next: string) {
  return next.startsWith("/") ? next : "/app";
}
