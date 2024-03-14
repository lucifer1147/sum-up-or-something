<script>
	import { activationdone } from './store.js';

	export let data;

	const handleSubmit = async () => {
		let uid = data.uid;
		let token = data.token;

		let request_data = {
			method: 'post',
			headers: {
				'content-type': 'application/json'
			},
			body: JSON.stringify({
				uid: uid,
				token: token
			})
		};

		let success = false;

		let base_url = 'http://127.0.0.1:8000/auth/api/users/activation/';
		let response = await fetch(base_url, request_data);
		if (response.ok) {
			success = true;
		}

		let resp = response.json();
		let errors = {};

		if (success !== true) {
			for (const [key, value] of Object.entries(resp)) {
				errors[key] = value;
			}
		} else {
			activationdone.set(true);
			window.location = 'http://localhost:5173/' + 'login'
		}
	};
</script>

<div
	class="bg-gradient-to-l from-slate-900 to-slate-800 h-[100vh] flex justify-center items-center backdrop-blur-lg"
>
	<div
		class="bg-white backdrop-opacity-45 w-2/3 h-1/2 rounded-2xl flex justify-center items-center flex-wrap"
	>
		{#if !$activationdone}
			<p class="text-3xl font-black w-full text-center opacity-100">
				Click here to activate your account
			</p>
			<button
				class="w-full h-20 text-2xl font-bold bg-slate-800 mx-10 rounded-xl text-white"
				on:click={handleSubmit}>Activate Account</button
			>
		{:else}
			<p class="text-5xl font-black w-full text-center opacity-100">
				Your Account has been Successfully Activated!
			</p>
		{/if}
	</div>
</div>
