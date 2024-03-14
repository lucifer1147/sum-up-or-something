import tokens from '$lib/shared/store/jwt.js';
import { browser } from '$app/environment';
import { redirect } from '@sveltejs/kit';

export const load = async ({ fetch, params }) => {
    const loadUserData = async (tokens) => {
        let success = false;
        let json;

        if (tokens !== null) {
            let request_data = {
                headers: {
                    'Authorization': `Bearer ${tokens.access}`
                }
            }


            let response = await fetch('http://localhost:8000/auth/api/users/me/', request_data)
            if (response.ok) {
                success = true;
            }
            json = await response.json()

        }

        return {
            json: json,
            status: success,
        }
    }

    if (browser) {
        let userData = await loadUserData(tokens)
        if (userData.status === true) {
            throw redirect(303, '/dashboard')
        }
    }
}