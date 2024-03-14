<script>
	import { enhance } from '$app/forms';
	import { emailsent } from './store.js';

	let email = '';

	const updateFormData = (event, target) => {
		if (target === 'email') {
			email = event.target.value;
		}
	};

	const handleSubmit = async () => {
		let success = false;
        console.log(email)

		let base_url = 'http://localhost:8000/auth/api/users/reset_password/';
		let data = {
			method: 'post',
			headers: {
				'content-type': 'application/json'
			},
			body: JSON.stringify({
				email: email
			})
		};

		let response = await fetch(base_url, data);
		if (response.ok) {
			success = true;
		}
		let resp = await response.json();
		if (success === true) {
			emailsent.set(true);
		} else {
			let errors = {};
			for (const [key, value] of Object.entries(resp)) {
				errors[key] = value;
			}
		}
	};
</script>

<div
	class="bg-gradient-to-r from-slate-700 to-slate-900 h-[100vh] w-full flex justify-center items-center"
>
	<div class="h-2/3 w-1/2 bg-white rounded-xl flex justify-center items-center flex-wrap">
		{#if !$emailsent}
			<h1 class="text-4xl font-black w-full text-center opacity-100">Reset Your Password</h1>
			<form on:submit={handleSubmit} class="w-2/3 h-1/2" method="post" use:enhance>
				Email
				<div class="h-12 mb-3 w-full rounded-lg border-2">
					<input
						type="email"
						name="userEmail"
						id="emailbox"
						class="font-mono h-full w-full rounded-lg bg-gray-100 px-5"
						value={email}
						placeholder="Enter your email here..."
						on:change={(e) => {
							updateFormData(e, 'email');
						}}
					/>
				</div>

				<button
					class="bg-slate-800 text-white font-mono font-bold text-lg h-12 w-full rounded-lg"
					type="submit">Reset Password</button
				>
			</form>
		{:else}
			<p class="text-4xl font-black w-full text-center opacity-100">
				Check your inbox to change your password.
			</p>
		{/if}
	</div>
</div>
