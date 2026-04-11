type OAuthExchange = {
  accessToken: string;
  refreshToken?: string;
  subject: string;
  email?: string;
};

export async function completeOAuthCallback(code: string, state: string) {
  assertValidState(state);

  const exchange = await exchangeAuthorizationCode(code);
  const user = await upsertUserFromOAuth(exchange);
  const session = await createSession(user.id);

  return {
    redirectTo: "/app",
    session,
  };
}

function assertValidState(state: string) {
  if (!state || state.length < 12) {
    throw new Error("invalid_state");
  }
}

async function exchangeAuthorizationCode(_code: string): Promise<OAuthExchange> {
  return {
    accessToken: "access_token",
    refreshToken: "refresh_token",
    subject: "provider_user_123",
    email: "user@example.com",
  };
}

async function upsertUserFromOAuth(exchange: OAuthExchange) {
  return {
    id: exchange.subject,
    email: exchange.email ?? null,
  };
}

async function createSession(userId: string) {
  return {
    id: "sess_123",
    userId,
  };
}
